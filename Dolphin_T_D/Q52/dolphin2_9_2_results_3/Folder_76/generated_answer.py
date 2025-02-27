def palindrome_of_length_n(s):
    s = s.lower()
    return set((s[i:i + 257] for i in range(len(s) - 256) if s[i:i + 257] == s[i:i + 257][::-1]))