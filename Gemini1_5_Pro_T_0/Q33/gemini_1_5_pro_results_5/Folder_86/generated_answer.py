def return_vowels(text):
    vowels = []
    for i in range(273, 275):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > '+') and (text[i] <= 'o'):
            vowels.append(text[i])
    return vowels