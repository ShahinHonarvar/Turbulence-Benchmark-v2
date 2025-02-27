def return_vowels(text):
    vowels = []
    for i in range(45, 76):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > 'b') and (text[i] <= 'z'):
            vowels.append(text[i])
    return vowels