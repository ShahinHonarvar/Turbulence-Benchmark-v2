def return_vowels(text):
    vowels = []
    for i in range(45, 76):
        if i < len(text) and text[i] in 'aeiou' and (text[i].lower() > 'b') and (text[i].lower() <= 'z'):
            vowels.append(text[i])
    return vowels