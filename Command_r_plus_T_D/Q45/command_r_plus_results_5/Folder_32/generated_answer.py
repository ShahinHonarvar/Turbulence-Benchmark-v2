def palindromes_between_indices(s: str) -> set:
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes