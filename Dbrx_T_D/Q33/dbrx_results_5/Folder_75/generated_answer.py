def return_vowels(s):
    vowels = []
    for i in range(20, 41):
        if 'K' < s[i] <= 'Z' and s[i] in 'AEIOU':
            vowels.append(s[i])
    return vowels