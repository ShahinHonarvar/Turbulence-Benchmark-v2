def return_vowels(str):
    vowels = []
    for i in range(21, 59):
        if str[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(str[i])
    return vowels