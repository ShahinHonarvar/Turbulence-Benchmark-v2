def return_vowels(text):
    vowels = []
    for i in range(29, 31):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > 'a') and (text[i] <= 'f'):
            vowels.append(text[i])
    return vowels