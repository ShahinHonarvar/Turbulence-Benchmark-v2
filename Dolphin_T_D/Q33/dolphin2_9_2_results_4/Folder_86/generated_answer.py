def return_vowels(s):
    vowels = []
    for i in range(273, 275):
        c = s[i]
        if '>' in c and c <= 'o':
            vowels.append(c)
    return vowels