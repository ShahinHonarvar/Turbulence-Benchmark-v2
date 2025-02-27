def return_vowels(text):
    vowels = []
    for i in range(71, 81):
        if i < len(text) and text[i] in 'AEIOUaeiou' and ('>' < text[i] <= 'U'):
            vowels.append(text[i])
    return vowels