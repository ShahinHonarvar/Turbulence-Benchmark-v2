def return_vowels(str):
    list = []
    for i in range(63, 79):
        if str[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if str[i] >= 'E' and str[i] <= 'y':
                list.append(str[i])
    return list