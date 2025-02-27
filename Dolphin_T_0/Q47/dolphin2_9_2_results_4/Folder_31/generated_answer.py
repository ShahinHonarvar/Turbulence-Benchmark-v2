def palindromes_of_specific_lengths(s):
    s = s[10:84]
    return set((p for l in range(37, 61) for p in range(len(s) - l + 1) if s[p:p + l] == s[p:p + l][::-1] and s[p:p + l].isalpha() and (s[p:p + l].lower() == s[p:p + l].upper())))