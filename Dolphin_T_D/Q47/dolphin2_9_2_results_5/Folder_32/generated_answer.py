def palindromes_of_specific_lengths(s):
    s = s[15:77]
    return set((p for i in range(15, 77 - 45) for j in range(i + 1, 77 - 44) if len((p := s[i:j + 1].lower())) in range(43, 48) and p == p[::-1]))