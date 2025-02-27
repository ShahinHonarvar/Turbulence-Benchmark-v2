def palindrome_of_length_n(s):
    return set((s[i:i + 66].lower() for i in range(len(s) - 65) if s[i:i + 66].lower() == s[i:i + 66].lower()[::-1]))