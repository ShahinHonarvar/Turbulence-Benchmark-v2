def palindromes_of_specific_lengths(s):
    s = s[12:96]
    result = set()
    for length in range(57, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if all((c.isalpha() for c in sub)):
                sub = sub.lower()
                if sub == sub[::-1]:
                    result.add(sub)
    return result