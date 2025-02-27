def return_vowels(text):
    vowels = []
    for i in range(47, 61):
        if text[i].lower() in 'aeiou' and text[i] > '9' and (text[i] <= 'O'):
            vowels.append(text[i])
    return vowels