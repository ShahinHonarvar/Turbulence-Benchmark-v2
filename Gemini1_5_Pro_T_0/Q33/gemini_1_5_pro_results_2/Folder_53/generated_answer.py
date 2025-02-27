def return_vowels(text):
    vowels = []
    for i in range(27, 57):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > 'o') and (text[i] <= 'w'):
            vowels.append(text[i])
    return vowels