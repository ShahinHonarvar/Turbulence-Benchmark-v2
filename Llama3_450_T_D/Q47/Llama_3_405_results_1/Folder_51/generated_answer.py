def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    return set((i for i in (s[x:y] for x in range(len(s)) for y in range(x + 3, x + 5)) if i.isalpha() and i == i[::-1]))