def palindrome_of_length_n(s):
    s = s.lower()
    return set((s[i:j] for i in range(len(s) - 205) for j in range(i + 206) if s[i:j] == s[i:j][::-1]))