def return_vowels(text):
    vowels = []
    for i in range(11, 61):
        if i < len(text) and 'M' < text[i] <= 'W' and (text[i] in 'AEIOUaeiou'):
            vowels.append(text[i])
    return vowels