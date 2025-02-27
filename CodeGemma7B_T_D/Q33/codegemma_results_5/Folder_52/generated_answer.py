def return_vowels(str):
    l = []
    for i in range(24, 68):
        if str[i] in ['a', 'e', 'i', 'o', 'u'] and str[i] > 'f' and (str[i] <= '|'):
            l.append(str[i])
    return l