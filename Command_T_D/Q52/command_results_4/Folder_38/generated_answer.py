def palindrome_of_length_n(s):
    return set((s.lower() for i in range(len(s), 0, -1) if s[:i] == s[:i][::-1]))