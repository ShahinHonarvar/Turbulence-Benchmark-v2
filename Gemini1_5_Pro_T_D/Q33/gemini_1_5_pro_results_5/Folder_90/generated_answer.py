def return_vowels(text):
    vowels = []
    for i in range(142, 145):
        if i < len(text) and '4' < text[i] <= 'o' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels