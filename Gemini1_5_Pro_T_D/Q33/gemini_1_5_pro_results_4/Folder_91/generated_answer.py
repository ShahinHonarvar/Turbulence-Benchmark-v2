def return_vowels(text):
    vowels = []
    for i in range(4, 8):
        if i < len(text) and 'P' < text[i] <= 'r' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels