def return_vowels(s):
    vowels = []
    for i in range(1, 9):
        if s[i] >= '?' and s[i] <= 'k' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels