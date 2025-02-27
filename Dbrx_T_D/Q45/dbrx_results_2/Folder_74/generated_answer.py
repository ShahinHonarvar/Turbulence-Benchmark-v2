def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(1, len(s), 5):
        for j in range(i + 1, min(i + 6, len(s)) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 6:
                palindromes.add(substring)
    return palindromes