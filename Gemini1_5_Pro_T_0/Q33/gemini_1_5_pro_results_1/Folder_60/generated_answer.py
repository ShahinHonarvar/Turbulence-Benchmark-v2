def return_vowels(s):
    vowels = []
    for i in range(24, 59):
        if i < len(s) and s[i] in 'OUE' and (s[i] >= 'N'):
            vowels.append(s[i])
    return vowels