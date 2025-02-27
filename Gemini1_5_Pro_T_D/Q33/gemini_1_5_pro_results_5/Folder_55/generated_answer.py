def return_vowels(text):
    vowels = []
    for i in range(1, min(5, len(text))):
        if text[i] in 'aeiouAEIOU' and '!' < text[i] <= 'j':
            vowels.append(text[i])
    return vowels