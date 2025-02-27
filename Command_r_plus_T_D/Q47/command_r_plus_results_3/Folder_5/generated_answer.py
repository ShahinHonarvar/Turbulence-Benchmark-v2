def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[62:71].lower()
    for i in range(63, 67):
        for j in range(i + 3, 71):
            word = substring[i:j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes