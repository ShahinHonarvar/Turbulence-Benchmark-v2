def return_vowels(text):
    vowels = []
    for i in range(1, min(9, len(text))):
        if text[i] in 'aeiouAEIOU' and '?' < text[i] <= 'k':
            vowels.append(text[i])
    return vowels