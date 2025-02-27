def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(18, 99):
        for j in range(i + 30, 99):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes