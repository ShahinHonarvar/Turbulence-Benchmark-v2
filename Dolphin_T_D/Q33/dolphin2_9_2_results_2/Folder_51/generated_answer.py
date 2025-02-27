def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    res = []
    for c in s[56:68]:
        if vowels.count(c) > 0 and c > 'M' and (c <= 'X'):
            res.append(c)
    return res