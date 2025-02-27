def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(273, 275):
        if text[i] in vowels and text[i] > '+' and (text[i] <= 'o'):
            result.append(text[i])
    return result