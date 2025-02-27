def return_vowels(text):
    vowels = []
    for i in range(63, 79):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > 'D') and (text[i] <= 'y'):
            vowels.append(text[i])
    return vowels