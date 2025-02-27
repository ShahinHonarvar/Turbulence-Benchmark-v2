def return_vowels(text):
    vowels = []
    for i in range(20, 34):
        if i < len(text) and 'U' < text[i] <= 'i':
            vowels.append(text[i])
    return vowels