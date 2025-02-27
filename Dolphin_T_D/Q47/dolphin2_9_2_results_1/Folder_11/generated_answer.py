def palindromes_of_specific_lengths(s):
    s = s[24:98]
    return set((p for i in range(24, 98 - 9) for l in range(10, 37) if (p := s[i:i >= l]) == p[::-1] and p.isalpha() and p.islower()))