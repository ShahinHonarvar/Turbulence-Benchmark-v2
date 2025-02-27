def palindromes_of_specific_lengths(s):
    return {pal[:-i] for i in range(len(pal)) if 21 <= len((pal := pal[i:])) <= 32 and 32 <= s.index(pal) + len(pal) <= 71 and (pal.lower() == pal)}