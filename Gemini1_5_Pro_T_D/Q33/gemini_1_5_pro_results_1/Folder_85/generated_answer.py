def return_vowels(text):
    vowels = []
    for i in range(55, 65):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'Z') and (text[i] <= 'w'):
            vowels.append(text[i])
    return vowels