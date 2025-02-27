def palindrome_of_length_n(s):
    s = s.lower()
    return set((s[i:i + 3] for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i].isalpha() and s[i + 1].isalpha() and s[i + 2].isalpha()))