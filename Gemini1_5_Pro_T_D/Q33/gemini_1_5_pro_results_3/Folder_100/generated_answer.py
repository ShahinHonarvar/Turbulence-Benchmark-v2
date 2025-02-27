def return_vowels(s):
    vowels = []
    for i in range(23, 75):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (s[i] > 'L') and (s[i] <= 'd'):
            vowels.append(s[i])
    return vowels