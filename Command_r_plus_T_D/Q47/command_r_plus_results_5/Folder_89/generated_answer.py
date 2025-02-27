def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[18:89]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 15, len(substring))):
            word = substring[i:j]
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes