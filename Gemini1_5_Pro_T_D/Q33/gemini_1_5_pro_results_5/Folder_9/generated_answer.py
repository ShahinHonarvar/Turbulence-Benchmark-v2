def return_vowels(text):
    vowels = []
    for i in range(13, 35):
        if i < len(text) and '8' < text[i] <= 'F' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels