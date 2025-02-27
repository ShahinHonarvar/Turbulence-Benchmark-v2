def return_vowels(text):
    vowels = []
    for i in range(23, 57):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('0' < text[i] <= 'd'):
            vowels.append(text[i])
    return vowels