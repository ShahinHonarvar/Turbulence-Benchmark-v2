def return_vowels(s):
    vowels = []
    for i in range(22, 82):
        if s[i] > 'N' and s[i] <= 'o' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels