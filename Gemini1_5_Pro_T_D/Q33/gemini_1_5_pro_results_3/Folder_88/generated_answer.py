def return_vowels(text):
    vowels = []
    for i in range(70, 76):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > text[2]) and (text[i] <= ':'):
            vowels.append(text[i])
    return vowels