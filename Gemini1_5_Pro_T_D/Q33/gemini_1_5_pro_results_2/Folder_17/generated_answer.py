def return_vowels(text):
    vowels = []
    for i in range(60, 99):
        if i < len(text) and text[i] in 'aeiou' and ('j' < text[i] <= 'n'):
            vowels.append(text[i])
    return vowels