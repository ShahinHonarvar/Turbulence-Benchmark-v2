def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[26:78].lower()
    palindromes = set()
    for i in range(len(substring) - 17):
        for j in range(2):
            word = substring[i:i + 18 + j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes