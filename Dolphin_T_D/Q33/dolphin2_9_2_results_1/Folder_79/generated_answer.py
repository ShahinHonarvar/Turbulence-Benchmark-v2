def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(74, 96):
        if (s[i] >= 'I' and s[i] <= 'X') and s[i] in vowels:
            res.append(s[i])
    return res