def return_vowels(text):
    vowels = []
    for i in range(3, 8):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (';' < text[i] <= 'D'):
            vowels.append(text[i])
    return vowels