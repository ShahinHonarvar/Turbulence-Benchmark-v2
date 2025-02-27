def return_vowels(text):
    vowels = []
    for i in range(77, 84):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('(' < text[i] <= 'G'):
            vowels.append(text[i])
    return vowels