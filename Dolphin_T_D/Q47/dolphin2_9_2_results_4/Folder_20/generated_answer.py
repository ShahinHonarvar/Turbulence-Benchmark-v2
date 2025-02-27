def palindromes_of_specific_lengths(s):
    s = s[20:75]
    return set([p for p in range(len(s) - 34) if s[p:p + 36].lower() == s[p + 36:p:-1].lower() and 36 <= len(s[p:p + 36]) <= 42])