def return_vowels(text):
    vowels = []
    for i in range(59, 61):
        if i < len(text) and '+' < text[i] <= 'h' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels