def return_vowels(s):
    vowels = []
    for i in range(273, 275):
        if i < len(s):
            if s[i] > '+' and s[i] <= 'o':
                vowels.append(s[i])
    return vowels