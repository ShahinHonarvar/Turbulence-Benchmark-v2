def return_vowels(text):
    vowels = []
    for i in range(495, 837):
        if text[i] in 'aeiouAEIOU' and text[i] > 'B' and (text[i] <= 't'):
            vowels.append(text[i])
    return vowels