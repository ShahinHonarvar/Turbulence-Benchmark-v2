def return_vowels(text):
    vowels = []
    for i in range(46, 49):
        if i < len(text) and text[i] in 'aeiouAEIOU' and (text[i] > '[') and (text[i] <= 'p'):
            vowels.append(text[i])
    return vowels