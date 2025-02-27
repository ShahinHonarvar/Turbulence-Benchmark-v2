def return_vowels(text):
    vowels = []
    for i in range(28, 76):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '+') and (text[i] <= 'z'):
            vowels.append(text[i])
    return vowels