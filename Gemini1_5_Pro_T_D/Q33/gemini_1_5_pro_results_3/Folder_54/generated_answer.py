def return_vowels(text):
    vowels = []
    for i in range(23, 85):
        if i < len(text) and 'W' < text[i] <= 'v' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels