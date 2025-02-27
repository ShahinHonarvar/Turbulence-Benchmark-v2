def palindromes_of_specific_lengths(s):
    s = s[43:96]
    pal = set()
    for i in range(18, 48):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                pal.add(sub.lower())
    return pal