def return_vowels(s):
    vowels = []
    for i in range(71, 81):
        if i < len(s) and s[i] > '>' and (s[i] <= 'U') and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels