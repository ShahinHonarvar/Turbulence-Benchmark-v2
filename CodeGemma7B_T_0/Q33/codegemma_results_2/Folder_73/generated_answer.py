def return_vowels(text):
    vowels = []
    for i in range(47, 89):
        if text[i].lower() in 'aeiou' and text[i] > '@' and (text[i] <= 'n'):
            vowels.append(text[i])
    return vowels