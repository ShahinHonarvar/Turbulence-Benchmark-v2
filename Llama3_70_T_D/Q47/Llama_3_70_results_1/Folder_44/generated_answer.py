def palindromes_of_specific_lengths(s):
    s = s.lower()
    return set((x for i in range(18, 99) for x in [s[i:i + 31 + j] for j in range(20) if s[i:i + 31 + j] == s[i:i + 31 + j][::-1] and s[i:i + 31 + j].isalpha()]))