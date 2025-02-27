def return_vowels(s):
    vowels = []
    for i in range(50, 77):
        if i < len(s) and s[i] in 'aeiouAEIOU' and ('#' < s[i] <= 'r'):
            vowels.append(s[i])
    return vowels