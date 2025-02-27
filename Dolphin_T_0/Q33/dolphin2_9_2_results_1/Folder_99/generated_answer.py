def return_vowels(s):
    vowels = 'aeiou'
    res = []
    for ch in s[323:526]:
        if '+' < ch <= ':' and ch in vowels:
            res.append(ch)
    return res