def return_vowels(text):
    vowels = []
    for i in range(85, 99):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '/') and (text[i] <= 'n'):
            vowels.append(text[i])
    return vowels