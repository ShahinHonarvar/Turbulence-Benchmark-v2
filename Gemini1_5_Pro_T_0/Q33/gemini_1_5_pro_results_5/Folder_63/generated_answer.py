def return_vowels(text):
    vowels = []
    for i in range(34, 69):
        if i < len(text) and text[i] in 'aeiou' and ('_' < text[i] <= 'o'):
            vowels.append(text[i])
    return vowels