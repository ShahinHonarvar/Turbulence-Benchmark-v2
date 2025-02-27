def return_vowels(text):
    vowels = []
    for i in range(24, 68):
        if text[i] in 'aeiouAEIOU' and text[i] > 'f' and (text[i] <= '|'):
            vowels.append(text[i])
    return vowels