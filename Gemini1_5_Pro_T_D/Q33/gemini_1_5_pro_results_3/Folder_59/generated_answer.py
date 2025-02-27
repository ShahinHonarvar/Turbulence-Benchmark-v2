def return_vowels(text):
    vowels = []
    for i in range(8, 9):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'Y') and (text[i] <= 's'):
            vowels.append(text[i])
    return vowels