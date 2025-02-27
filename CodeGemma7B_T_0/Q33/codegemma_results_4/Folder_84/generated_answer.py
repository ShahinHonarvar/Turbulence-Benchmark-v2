def return_vowels(text):
    vowels = []
    for i in range(770, 852):
        if text[i] in 'aeiouAEIOU' and text[i] > 'B' and (text[i] <= 'i'):
            vowels.append(text[i])
    return vowels