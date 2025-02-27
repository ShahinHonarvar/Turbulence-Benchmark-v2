def return_vowels(text):
    vowels = []
    for i in range(528, 606):
        if i < len(text) and text[i] in 'AEIOUaeiou' and ('M' < text[i] <= 'X'):
            vowels.append(text[i])
    return vowels