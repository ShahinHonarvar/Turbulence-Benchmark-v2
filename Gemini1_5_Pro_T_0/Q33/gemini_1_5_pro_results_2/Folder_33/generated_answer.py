def return_vowels(s):
    vowels = []
    for i in range(163, 771):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (s[i] > ':') and (s[i] <= 'E'):
            vowels.append(s[i])
    return vowels