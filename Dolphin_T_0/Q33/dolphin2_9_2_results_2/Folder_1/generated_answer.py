def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for i in range(24, 64):
        if 'f' < s[i] <= 'h':
            if s[i] in vowels:
                res.append(s[i])
    return res