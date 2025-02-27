def return_vowels(text):
    vowels = []
    for i in range(21, 59):
        if i < len(text) and text[i] in 'aeiou' and ('/' < text[i] <= 'a'):
            vowels.append(text[i])
    return vowels