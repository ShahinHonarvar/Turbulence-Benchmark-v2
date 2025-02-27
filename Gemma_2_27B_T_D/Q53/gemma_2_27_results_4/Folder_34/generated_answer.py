def palindrome_of_length_at_least_n(s):
    return {p for p in set((w for w in [s[i:j + 1] for i in range(len(s)) for j in range(i, len(s))] if len(w) >= 68 and w.lower() == w[::-1].lower()))}