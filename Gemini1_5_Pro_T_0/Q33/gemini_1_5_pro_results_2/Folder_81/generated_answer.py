def return_vowels(text):
    vowels = []
    for i in range(20, 43):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('5' < text[i] <= 'M'):
            vowels.append(text[i])
    return vowels