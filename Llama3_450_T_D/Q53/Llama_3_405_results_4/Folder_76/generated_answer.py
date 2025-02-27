def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return set((p for length in range(137, len(s) + 1) for i in range(len(s) - length + 1) if (p := s[i:i + length]) == p[::-1]))