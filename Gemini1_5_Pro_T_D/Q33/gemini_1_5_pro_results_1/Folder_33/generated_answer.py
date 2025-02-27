def return_vowels(text):
    vowels = []
    for i in range(163, 771):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > ':') and (text[i] <= 'E'):
            vowels.append(text[i])
    return vowels