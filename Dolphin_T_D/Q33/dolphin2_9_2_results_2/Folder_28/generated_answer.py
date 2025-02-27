def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for c in s[41:50]:
        if 'W' < c <= '[' and c in vowels:
            res.append(c)
    return res