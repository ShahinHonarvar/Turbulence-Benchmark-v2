def return_vowels(s):
    vowels = []
    for i in range(85, 99):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (s[i] > '/') and (s[i] <= 'n'):
            vowels.append(s[i])
    return vowels