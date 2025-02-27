def return_vowels(s):
    vowels = []
    for i in range(31, 37):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (';' < s[i] <= 't'):
            vowels.append(s[i])
    return vowels