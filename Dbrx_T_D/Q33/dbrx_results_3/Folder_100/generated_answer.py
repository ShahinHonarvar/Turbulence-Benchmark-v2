def return_vowels(s):
    vowels = []
    for i in range(23, 75):
        if s[i] > 'L' and s[i] <= 'd' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels