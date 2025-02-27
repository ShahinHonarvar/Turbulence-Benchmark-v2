def return_vowels(text):
    vowels = []
    for i in range(32, 61):
        if i < len(text) and '?' < text[i] <= 'P' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels