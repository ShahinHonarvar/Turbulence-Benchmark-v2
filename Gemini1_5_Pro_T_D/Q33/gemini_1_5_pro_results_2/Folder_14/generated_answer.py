def return_vowels(text):
    vowels = []
    for i in range(47, 61):
        if i < len(text) and '9' < text[i] <= 'O' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels