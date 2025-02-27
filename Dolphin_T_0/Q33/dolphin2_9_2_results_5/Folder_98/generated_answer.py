def return_vowels(s):
    vowels = []
    for i in range(3, 9):
        if 'S' < s[i] <= 'U' and s[i] in 'AEIOU':
            vowels.append(s[i])
    return vowels