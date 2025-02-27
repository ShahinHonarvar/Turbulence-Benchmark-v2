def return_vowels(text):
    vowels = list()
    for i in range(64, 82):
        if text[i] in 'aeiouAEIOU' and text[i] > 'P' and (text[i] <= 'z'):
            vowels.append(text[i])
    return vowels or []