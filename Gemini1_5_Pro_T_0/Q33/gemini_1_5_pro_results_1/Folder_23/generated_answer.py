def return_vowels(s):
    vowels = []
    for i in range(56, 96):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (s[i] > '&') and (s[i] <= 'T'):
            vowels.append(s[i])
    return vowels