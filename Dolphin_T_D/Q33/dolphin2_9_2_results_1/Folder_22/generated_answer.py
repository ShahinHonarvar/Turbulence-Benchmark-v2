def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for c in s[56:90]:
        if 'k' < c <= 'z' and c in vowels:
            res.append(c)
    return res