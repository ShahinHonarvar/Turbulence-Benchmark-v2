def return_vowels(str):
    vowels = []
    for i in range(464, 574):
        if str[i] in ['a', 'e', 'i', 'o', 'u'] and str[i] > 'a' and (str[i] <= 'g'):
            vowels.append(str[i])
    return vowels