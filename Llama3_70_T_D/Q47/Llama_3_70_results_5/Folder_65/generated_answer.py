def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    return set((c for length in range(20, 67) for i in range(len(s) - length + 1) if (c := s[i:i + length]) == c[::-1] and c.isalpha()))