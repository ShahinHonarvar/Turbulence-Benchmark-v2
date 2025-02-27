def return_vowels(s):
    vowels = []
    for i in range(21, 59):
        if s[i] > '/' and s[i] <= 'a' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels