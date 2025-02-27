def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s.lower() if c.isalpha()))
    n = 18
    return set((s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]))