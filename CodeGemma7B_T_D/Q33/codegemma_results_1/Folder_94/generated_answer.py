def return_vowels(text):
    vowels = []
    for i in range(40, 94):
        if text[i] in ['a', 'e', 'i', 'o', 'u'] and text[i] > '4' and (text[i] <= 'H'):
            vowels.append(text[i])
    return vowels