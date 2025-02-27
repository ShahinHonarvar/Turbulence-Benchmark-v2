def return_vowels(text):
    vowels = []
    for i in range(32, 61):
        if text[i] in 'AEIOUaeiou' and text[i] > '?' and (text[i] <= 'P'):
            vowels.append(text[i])
    return vowels