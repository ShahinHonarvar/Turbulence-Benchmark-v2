def return_vowels(text):
    vowels = []
    for i in range(29, 31):
        if text[i].lower() in 'aeiou' and text[i] > 'a' and (text[i] <= 'f'):
            vowels.append(text[i])
    return vowels