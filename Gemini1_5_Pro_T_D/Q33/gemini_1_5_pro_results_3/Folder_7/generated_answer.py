def return_vowels(text):
    vowels = []
    for i in range(202, 872):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('3' < text[i] <= '>'):
            vowels.append(text[i])
    return vowels