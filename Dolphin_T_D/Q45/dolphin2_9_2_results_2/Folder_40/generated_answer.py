def palindromes_between_indices(s):
    substring = ''.join((ch.lower() for ch in s if 4 <= s.index(ch) <= 9))
    return set((pal for length in range(7, len(substring) + 1) for pal in set(substring.combinations(length)) if pal == pal[::-1]))