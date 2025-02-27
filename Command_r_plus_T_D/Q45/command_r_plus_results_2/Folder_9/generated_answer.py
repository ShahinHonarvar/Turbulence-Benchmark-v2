def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    chars = [c for c in s[:7] if c.isalpha()]
    chars_lower = [c.lower() for c in chars]
    for p in range(7, len(chars_lower) * 2 + 1):
        for i in range(len(chars_lower) - p + 1):
            substring = chars_lower[i:i + p]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring).upper())
    return palindromes