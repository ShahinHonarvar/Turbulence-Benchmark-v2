def return_vowels(text):
    vowels = []
    for i in range(1, 5):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('!' < text[i] <= 'j'):
            vowels.append(text[i])
    return vowels