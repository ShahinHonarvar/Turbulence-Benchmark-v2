def return_vowels(text):
    vowels = []
    for i in range(71, 81):
        if text[i] in 'aeiouAEIOU' and text[i] > '>' and (text[i] <= 'U'):
            vowels.append(text[i])
    return vowels