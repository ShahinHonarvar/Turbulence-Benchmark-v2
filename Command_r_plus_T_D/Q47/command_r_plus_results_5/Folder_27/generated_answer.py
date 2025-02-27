def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(13, 100 - 26):
        for j in range(26, 30):
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes