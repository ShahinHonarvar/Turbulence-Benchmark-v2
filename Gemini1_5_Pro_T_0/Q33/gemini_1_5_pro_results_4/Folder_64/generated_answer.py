def return_vowels(text):
    vowels = []
    for i in range(1, 7):
        if i < len(text) and 'F' < text[i] <= 'j' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels