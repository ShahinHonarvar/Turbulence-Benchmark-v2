def return_vowels(text):
    vowels = []
    for i in range(31, 37):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > ';') and (text[i] <= 't'):
            vowels.append(text[i])
    return vowels