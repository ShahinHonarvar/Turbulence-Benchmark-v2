def return_vowels(text):
    vowels = []
    for i in range(3, 9):
        if i < len(text) and text[i] in 'AEIOU' and ('S' < text[i] <= 'U'):
            vowels.append(text[i])
    return vowels