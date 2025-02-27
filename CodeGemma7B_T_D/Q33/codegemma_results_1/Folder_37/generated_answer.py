def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(82, 90):
        if s[i] in vowels and s[i] > 'T' and (s[i] <= 'b'):
            res.append(s[i])
    return res