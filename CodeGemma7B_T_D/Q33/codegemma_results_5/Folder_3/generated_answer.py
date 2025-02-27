def return_vowels(s):
    vowels = []
    for i in range(50, 77):
        if s[i] in ['a', 'e', 'i', 'o', 'u'] and s[i] >= '#' and (s[i] <= 'r'):
            vowels.append(s[i])
    return vowels