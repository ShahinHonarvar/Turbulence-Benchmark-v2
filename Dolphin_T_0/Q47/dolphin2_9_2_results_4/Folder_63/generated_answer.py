def palindromes_of_specific_lengths(s):
    sub = s[32:85]
    return set(filter(lambda p: 26 <= len(p) <= 31, filter(lambda p: all((c.isalpha() or c.islower() for c in p)), set((p for p in sub if sub == sub[::-1])))))