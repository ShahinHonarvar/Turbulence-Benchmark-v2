def return_vowels(text):
    vowels = []
    for i in range(40, 94):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '4') and (text[i] <= 'H'):
            vowels.append(text[i])
    return vowels