def return_vowels(text):
    vowels = []
    for i in range(24, 59):
        if i < len(text) and text[i] in 'OOU':
            vowels.append(text[i])
    return vowels