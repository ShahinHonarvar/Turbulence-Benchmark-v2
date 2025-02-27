import re
        from itertools import groupby

def palindromes_of_specific_lengths(s):
    if len(s) <= 300 and len(s) >= 100:
        s = s.lower()
        l = list(s)
        g = groupby(l)
        backwards1 = [y for x, y in g if y in 'abcdefghijklmnopqrstuvwxyz']
        backwards2 = [x for x, y in g if y in 'abcdefghijklmnopqrstuvwxyz']
        backwards3 = backwards2[::-1]
        if backwards1 == backwards3:
            for i in range(len(s)):
                if len(s[i + 1:]) >= 49 and len(s[i + 1:]) <= 100:
                    if s[i + 1:] == s[i + 1:][::-1]:
                        if re.fullmatch('[a-z]+', s[i + 1:]):
                            return {s[i:i + len(s[i + 1:]) + 1]}
    return set()