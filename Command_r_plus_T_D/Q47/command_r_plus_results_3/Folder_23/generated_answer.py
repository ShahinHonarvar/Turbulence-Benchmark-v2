def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(23, 95):
        for j in range(i + 16, 95):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes