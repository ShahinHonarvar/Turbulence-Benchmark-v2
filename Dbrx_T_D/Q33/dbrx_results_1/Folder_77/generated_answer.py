def return_vowels(s):
    vowels = []
    for i in range(837, 975):
        if s[i] > 'N' and s[i] <= 'W' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels