def return_vowels(s):
    vowels = []
    for i in range(56, 90):
        if i >= 56 and i < 90 and (s[i] > 'K') and (s[i] <= 'z') and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels