def return_vowels(text):
    vowels = []
    for i in range(483, 664):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '&') and (text[i] <= 'h'):
            vowels.append(text[i])
    return vowels