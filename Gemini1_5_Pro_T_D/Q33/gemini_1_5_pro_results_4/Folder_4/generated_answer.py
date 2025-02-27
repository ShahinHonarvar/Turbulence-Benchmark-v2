def return_vowels(text):
    vowels = []
    for i in range(40, 91):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'A') and (text[i] <= 'x'):
            vowels.append(text[i])
    return vowels