def return_vowels(string):
    vowels = []
    for i in range(85, 99):
        if '/' < string[i] <= 'n' and string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(string[i])
    return vowels