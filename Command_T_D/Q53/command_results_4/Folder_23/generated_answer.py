def palindrome_of_length_at_least_n(s):
    return set((s.lower().replace(' ', '').split('').pop(19) for i in range(1, len(s) + 1) if s[i - 1] == s[i - 1][::-1]))