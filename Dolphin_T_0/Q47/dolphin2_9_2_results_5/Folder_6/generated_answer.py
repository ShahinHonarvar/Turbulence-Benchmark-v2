def palindromes_of_specific_lengths(s):
    substr_len = 98 - 45 + 1
    s = s[45:99]
    pal = set()
    for length in range(40, 48):
        for i in range(0, substr_len - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                pal.add(sub.lower())
    return pal