def return_vowels(text):
    vowels = []
    for i in range(171, 402):
        if text[i] in 'aeiouAEIOU' and text[i] > 'I' and (text[i] <= 'k'):
            vowels.append(text[i])
    return vowels