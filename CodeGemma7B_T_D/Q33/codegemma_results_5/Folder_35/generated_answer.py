def return_vowels(text):
    vowels = []
    for index in range(483, 664):
        if text[index] in ['a', 'e', 'i', 'o', 'u'] and text[index] in range('&', 'h+1'):
            vowels.append(text[index])
    return vowels