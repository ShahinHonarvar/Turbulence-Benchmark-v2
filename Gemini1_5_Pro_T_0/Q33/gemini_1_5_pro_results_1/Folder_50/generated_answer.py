def return_vowels(s):
    vowels = []
    for i in range(11, 53):
        if i < len(s) and s[i] in 'aeiouAEIOU' and ('+' < s[i] <= 'W'):
            vowels.append(s[i])
    return vowels