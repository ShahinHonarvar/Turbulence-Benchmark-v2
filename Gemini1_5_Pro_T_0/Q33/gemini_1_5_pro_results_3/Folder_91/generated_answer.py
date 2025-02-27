def return_vowels(text):
    vowels = []
    for i in range(4, 8):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('P' < text[i] <= 'r'):
            vowels.append(text[i])
    return vowels