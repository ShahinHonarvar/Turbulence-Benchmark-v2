def return_vowels(string):
    vowels = []
    for i in range(273, 275):
        if i < len(string) and string[i] > '+' and (string[i] <= 'o') and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels