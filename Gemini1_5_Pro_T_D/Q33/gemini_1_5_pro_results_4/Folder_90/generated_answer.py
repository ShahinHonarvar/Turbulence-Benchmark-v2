def return_vowels(text):
    vowels = []
    for i in range(142, 145):
        if i < len(text) and text[i] in 'aeiou' and ('4' < text[i] <= 'o'):
            vowels.append(text[i])
    return vowels