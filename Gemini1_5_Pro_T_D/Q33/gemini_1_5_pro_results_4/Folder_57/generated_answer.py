def return_vowels(text):
    vowels = []
    for i in range(21, 23):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('-' < text[i] <= 'n'):
            vowels.append(text[i])
    return vowels