def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    candidates = set((s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)))
    palindromes = set((word for word in candidates if word == word[::-1] and len(word) >= 150))
    return palindromes