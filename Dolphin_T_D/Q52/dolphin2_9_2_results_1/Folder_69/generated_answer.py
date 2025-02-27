def palindrome_of_length_n(s):
    s = filter(str.isalpha, s.lower())
    return set((s[i:j] for i in range(len(s)) for j in range(i + 472, len(s) + 1) if s[i:j] == s[i:j][::-1]))