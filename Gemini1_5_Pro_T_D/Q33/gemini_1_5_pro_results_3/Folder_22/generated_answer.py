def return_vowels(text):
    vowels = []
    for i in range(56, 90):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'K') and (text[i] <= 'z'):
            vowels.append(text[i])
    return vowels