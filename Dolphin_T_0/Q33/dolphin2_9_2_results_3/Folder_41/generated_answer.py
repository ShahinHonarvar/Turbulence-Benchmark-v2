def return_vowels(s):
    vowels = []
    for i in range(71, 81):
        if '>' < s[i] <= 'U':
            vowels.append(s[i])
    return vowels