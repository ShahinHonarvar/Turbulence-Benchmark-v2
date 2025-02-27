def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for i in range(56, 68):
        if vowels.count(s[i].lower()) > 0 and s[i] > 'M' and (s[i] <= 'X'):
            res.append(s[i])
    return res