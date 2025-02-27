def return_vowels(s):
    vowels = []
    for i in range(60, 99):
        if s[i] > 'j' and s[i] <= 'n' and (s[i] in ['a', 'e', 'i', 'o', 'u']):
            vowels.append(s[i])
    return vowels