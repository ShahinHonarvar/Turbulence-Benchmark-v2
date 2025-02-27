def return_vowels(text):
    vowels = []
    for i in range(23, 38):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'N') and (text[i] <= 'k'):
            vowels.append(text[i])
    return vowels