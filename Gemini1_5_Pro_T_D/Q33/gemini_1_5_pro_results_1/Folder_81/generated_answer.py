def return_vowels(text):
    vowels = []
    for i in range(20, 43):
        if i < len(text) and '5' < text[i] <= 'M' and (text[i] in 'AEIOUaeiou'):
            vowels.append(text[i])
    return vowels