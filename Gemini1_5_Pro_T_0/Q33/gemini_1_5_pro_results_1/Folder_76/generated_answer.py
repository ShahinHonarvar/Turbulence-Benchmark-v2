def return_vowels(text):
    vowels = []
    for i in range(495, 837):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('B' < text[i] <= 't'):
            vowels.append(text[i])
    return vowels