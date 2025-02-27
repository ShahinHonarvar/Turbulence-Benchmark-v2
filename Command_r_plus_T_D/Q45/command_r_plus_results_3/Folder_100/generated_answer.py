def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    s_lower = s[:6].lower()
    for i in range(len(s_lower)):
        for j in range(i + 6, len(s_lower) + 1):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes