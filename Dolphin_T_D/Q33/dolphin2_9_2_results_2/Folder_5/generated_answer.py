def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for i in range(44, 95):
        if s[i] in vowels and 5 < s[i] < '<':
            res.append(s[i])
    return res