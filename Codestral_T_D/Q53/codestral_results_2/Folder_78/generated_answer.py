def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 96
    return set((w for w in [s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1)] if w == w[::-1] and w.isalpha()))