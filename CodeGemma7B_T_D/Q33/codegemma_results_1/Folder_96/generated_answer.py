def return_vowels(text):
    vowels = []
    for i in range(77, 84):
        if text[i] in 'aeiouAEIOU' and text[i] in range('(', 'H'):
            vowels.append(text[i])
    return vowels