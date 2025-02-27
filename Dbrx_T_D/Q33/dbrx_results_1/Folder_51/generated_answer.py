def return_vowels(s):
    vowels = []
    for i in range(56, 68):
        if s[i] > 'M' and s[i] <= 'X' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels