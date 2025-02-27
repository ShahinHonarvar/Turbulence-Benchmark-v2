def palindrome_of_length_n(s):
    s = s.lower()
    return set((p for i in range(len(s) - 96) for p in [s[i:i + 97]] if p == p[::-1] and p.isalpha()))