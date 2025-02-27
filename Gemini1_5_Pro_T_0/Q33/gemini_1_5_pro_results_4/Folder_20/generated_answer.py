def return_vowels(text):
    vowels = []
    for i in range(59, 61):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('+' < text[i] <= 'h'):
            vowels.append(text[i])
    return vowels