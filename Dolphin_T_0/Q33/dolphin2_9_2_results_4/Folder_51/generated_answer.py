def return_vowels(s):
    vowels = []
    for i in range(56, 68):
        if 'M' < s[i] <= 'X' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels