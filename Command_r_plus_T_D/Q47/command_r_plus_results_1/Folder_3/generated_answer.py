def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[26:96].lower()
    for i in range(27, len(substring) - 48):
        for j in range(i + 49, min(i + 52, len(substring) + 1)):
            word = substring[i:j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes