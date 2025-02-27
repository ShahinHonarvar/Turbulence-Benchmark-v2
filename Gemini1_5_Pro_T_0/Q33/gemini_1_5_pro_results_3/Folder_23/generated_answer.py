def return_vowels(text):
    vowels = []
    for i in range(56, 96):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '&') and (text[i] <= 'T'):
            vowels.append(text[i])
    return vowels