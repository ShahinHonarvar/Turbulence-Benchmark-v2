def return_vowels(text):
    vowels = []
    for i in range(604, 949):
        if text[i] in 'aeiouAEIOU' and text[i] > 'N' and (text[i] <= 'U'):
            vowels.append(text[i])
    return vowels