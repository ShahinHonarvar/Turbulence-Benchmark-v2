def palindromes_of_specific_lengths(s):
    pair = set()
    s = s[10:97]
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub.lower())):
                pair.add(sub)
    return pair