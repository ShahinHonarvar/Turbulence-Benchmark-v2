def return_vowels(text):
    vowels = []
    for i in range(10, 83):
        if text[i] in 'aeiouAEIOU' and text[i] > '%' and (text[i] <= 'e'):
            vowels.append(text[i])
    return vowels