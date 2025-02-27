def return_vowels(text):
    vowels = []
    for i in range(20, 41):
        if i < len(text) and text[i] in 'AEIOU' and (text[i] > 'K') and (text[i] <= 'Z'):
            vowels.append(text[i])
    return vowels