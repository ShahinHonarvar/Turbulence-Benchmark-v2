def return_vowels(text):
    vowels = []
    for i in range(74, 96):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (text[i] > 'I') and (text[i] <= 'X'):
            vowels.append(text[i])
    return vowels