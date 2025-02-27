def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[:11].lower()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            word = substring[i:j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes