def return_vowels(s):
    vowels = []
    for i in range(50, 51):
        if s[i] > ',' and s[i] <= 'v' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels