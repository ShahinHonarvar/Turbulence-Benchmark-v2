def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    return set((p for length in range(7, 10) for i in range(len(s) - length + 1) if (p := s[i:i + length]).isalpha() and p == p[::-1]))