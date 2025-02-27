def palindromes_of_specific_lengths(s):
    sub = s[127:289]
    return set((p for p in sub if len(p) in range(119, 142) and p.lower() == p[::-1].lower()))