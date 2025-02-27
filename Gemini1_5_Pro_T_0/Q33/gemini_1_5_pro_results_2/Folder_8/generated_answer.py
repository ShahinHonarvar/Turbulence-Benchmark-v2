def return_vowels(text):
    vowels = []
    for i in range(64, 82):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'P') and (text[i] <= 'z'):
            vowels.append(text[i])
    return vowels