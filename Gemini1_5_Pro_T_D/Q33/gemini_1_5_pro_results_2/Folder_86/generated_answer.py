def return_vowels(string):
    vowels = []
    for i in range(273, 275):
        if i < len(string) and string[i] in 'aeiou' and ('+' < string[i] <= 'o'):
            vowels.append(string[i])
    return vowels