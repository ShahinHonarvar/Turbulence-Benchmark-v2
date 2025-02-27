def return_vowels(string):
    vowels = []
    for i in range(1, 5):
        if string[i] in ['a', 'e', 'i', 'o', 'u'] and string[i] > '!' and (string[i] <= 'j'):
            vowels.append(string[i])
    return vowels