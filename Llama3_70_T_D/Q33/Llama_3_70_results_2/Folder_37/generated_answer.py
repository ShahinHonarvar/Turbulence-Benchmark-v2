def return_vowels(s):
    vowels = []
    for i in range(82, 90):
        if i < len(s) and s[i] > 'T' and (s[i] <= 'b') and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels