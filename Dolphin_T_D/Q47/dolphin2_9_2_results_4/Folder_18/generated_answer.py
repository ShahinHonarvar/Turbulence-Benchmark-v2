def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    return {pal for i in range(13, 67) for pal in s.split() if pal == pal[::-1] and len(pal) == i}