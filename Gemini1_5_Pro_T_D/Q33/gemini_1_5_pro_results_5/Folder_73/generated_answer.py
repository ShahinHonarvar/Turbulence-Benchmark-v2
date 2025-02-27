def return_vowels(text):
    vowels = []
    for i in range(47, 89):
        if text[i] in 'aeiou' and '@' < text[i] <= 'n':
            vowels.append(text[i])
    return vowels