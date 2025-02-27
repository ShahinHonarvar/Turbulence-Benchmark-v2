def return_vowels(s):
    vowels = []
    for i in range(24, 59):
        if s[i] > 'N' and s[i] <= 'U' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels