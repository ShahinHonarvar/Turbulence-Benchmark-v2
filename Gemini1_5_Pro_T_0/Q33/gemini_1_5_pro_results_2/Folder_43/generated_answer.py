def return_vowels(text):
    vowels = []
    for i in range(22, 82):
        if i < len(text) and text[i] in 'aeiou' and (text[i] > 'N') and (text[i] <= 'o'):
            vowels.append(text[i])
    return vowels