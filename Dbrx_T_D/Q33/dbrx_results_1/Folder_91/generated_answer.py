def return_vowels(s):
    vowels = []
    for i in range(4, 8):
        if i < len(s) and 'P' < s[i] <= 'r' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels