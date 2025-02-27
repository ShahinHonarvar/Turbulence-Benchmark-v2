def return_vowels(text):
    vowels = []
    for i in range(23, 57):
        if i < len(text) and '0' < text[i] <= 'd' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels