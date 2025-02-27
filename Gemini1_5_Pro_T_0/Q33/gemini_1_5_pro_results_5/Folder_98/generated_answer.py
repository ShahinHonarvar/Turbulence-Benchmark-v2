def return_vowels(text):
    vowels = []
    for i in range(3, 9):
        if i < len(text) and 'S' < text[i] <= 'U' and (text[i] in 'AEIOU'):
            vowels.append(text[i])
    return vowels