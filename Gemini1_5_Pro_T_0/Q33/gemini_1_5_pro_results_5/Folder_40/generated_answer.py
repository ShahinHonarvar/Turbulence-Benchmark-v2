def return_vowels(text):
    vowels = []
    for i in range(2, 7):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('^' < text[i] <= 'd'):
            vowels.append(text[i])
    return vowels