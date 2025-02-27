def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for i in range(273, 275):
        if string[i] in vowels and string[i] > '+' and (string[i] <= 'o'):
            filtered_vowels.append(string[i])
    return filtered_vowels