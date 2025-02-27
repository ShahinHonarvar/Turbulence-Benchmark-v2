def return_vowels(text):
    vowels = []
    for i in range(37, 57):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '*') and (text[i] <= 'P'):
            vowels.append(text[i])
    return vowels