def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    candidates = set((s[i:j] for i in range(len(s)) for j in range(i + 150, len(s) + 1)))
    palindromes = {c for c in candidates if c == c[::-1] and c.isalpha()}
    return palindromes