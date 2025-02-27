def return_vowels(text):
    vowels = []
    for i in range(8, 9):
        if i < len(text) and 'Y' < text[i] <= 's' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels