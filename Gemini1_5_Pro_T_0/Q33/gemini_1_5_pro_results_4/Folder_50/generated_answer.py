def return_vowels(text):
    vowels = []
    for i in range(11, 53):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('+' < text[i] <= 'W'):
            vowels.append(text[i])
    return vowels