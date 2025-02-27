def return_vowels(text):
    vowels = []
    for i in range(837, 975):
        if i < len(text) and text[i] in 'AEIOU' and (text[i] > 'N') and (text[i] <= 'W'):
            vowels.append(text[i])
    return vowels