def return_vowels(text):
    vowels = []
    for i in range(483, 664):
        if text[i] in ['a', 'e', 'i', 'o', 'u'] and text[i] > '&' and (text[i] <= 'h'):
            vowels.append(text[i])
    return vowels