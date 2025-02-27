def return_vowels(text):
    vowels = []
    for i in range(71, 88):
        if i < len(text) and '9' < text[i] <= 'P' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels