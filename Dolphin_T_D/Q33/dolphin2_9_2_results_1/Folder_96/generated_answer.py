def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for c in s[77:84]:
        if '(' < c <= 'G' and c in vowels:
            res.append(c)
    return res