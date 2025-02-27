def return_vowels(text):
    vowels = []
    for i in range(20, 34):
        if i < len(text) and 'U' < text[i] <= 'i' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels