def return_vowels(text):
    vowels = []
    for i in range(1, min(5, len(text))):
        if '!' < text[i] <= 'j' and text[i] in 'aeiouAEIOU':
            vowels.append(text[i])
    return vowels