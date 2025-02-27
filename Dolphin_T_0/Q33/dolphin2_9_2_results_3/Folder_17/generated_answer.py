def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for i in range(60, 99):
        if 'j' < s[i] <= 'n' and s[i] in vowels:
            res.append(s[i])
    return res