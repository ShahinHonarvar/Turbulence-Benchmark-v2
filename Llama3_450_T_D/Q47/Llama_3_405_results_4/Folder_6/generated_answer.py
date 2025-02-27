def palindromes_of_specific_lengths(s):
    s = s[45:99].lower()
    return set((p for length in range(40, 48) for i in range(len(s) - length + 1) if (p := s[i:i + length]).isalpha() and p == p[::-1]))