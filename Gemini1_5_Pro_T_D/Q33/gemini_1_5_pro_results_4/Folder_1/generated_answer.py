def return_vowels(text):
    vowels = []
    for i in range(24, 64):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'F') and (text[i] <= 'h'):
            vowels.append(text[i])
    return vowels