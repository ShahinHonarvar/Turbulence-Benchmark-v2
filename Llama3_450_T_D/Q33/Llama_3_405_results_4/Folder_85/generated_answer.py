def return_vowels(s):
    vowels = []
    for i in range(55, 65):
        if i < len(s) and 'Z' < s[i] <= 'w' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels