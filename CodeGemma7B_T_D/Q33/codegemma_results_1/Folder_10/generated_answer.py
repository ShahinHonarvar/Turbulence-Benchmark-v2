def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(31, 38):
        if str[i] in vowels and str[i] > ';' and (str[i] <= 't'):
            res.append(str[i])
    return res