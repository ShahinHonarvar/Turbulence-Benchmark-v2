def palindrome_of_length_n(s):
    s = s.lower()
    return set((t for i in range(len(s) - 463) for j in range(i + 464) if s[i] + s[i + 1] + ... + s[j] == s[j] + ... + s[i]))