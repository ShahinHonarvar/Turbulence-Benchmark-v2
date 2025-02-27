def return_vowels(s):
    vowels = []
    for i in range(273, 275):
        if i < len(s) and s[i] > '+' and (s[i] <= 'o') and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels