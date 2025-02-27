def return_vowels(text):
    vowels = []
    for i in range(56, 68):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (text[i] > 'M') and (text[i] <= 'X'):
            vowels.append(text[i])
    return vowels