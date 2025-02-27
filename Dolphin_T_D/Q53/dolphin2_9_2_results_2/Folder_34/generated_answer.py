def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 68
    return set((s[i:j + 1] for i, j in zip(range(len(s)), range(n - 1, len(s))) if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha()))