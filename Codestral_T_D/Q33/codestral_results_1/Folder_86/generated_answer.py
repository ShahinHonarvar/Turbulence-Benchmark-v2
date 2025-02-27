def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o']
    result = []
    for i in range(273, 275):
        if i < len(string) and string[i] > '+' and (string[i] <= 'o') and (string[i] in vowels):
            result.append(string[i])
    return result