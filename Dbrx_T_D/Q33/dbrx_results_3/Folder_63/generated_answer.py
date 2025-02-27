def return_vowels(s):
    vowels = []
    for i in range(34, 69):
        if s[i] > '_' and s[i] <= 'o' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels