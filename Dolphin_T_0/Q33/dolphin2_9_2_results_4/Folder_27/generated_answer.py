def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(29, 31):
        if 'a' < s[i] <= 'f' and s[i] in vowels:
            res.append(s[i])
    return res