def return_vowels(text):
    vowels = []
    for i in range(41, 50):
        if i < len(text) and text[i] in 'AEIOUaeiou' and (text[i] > 'W') and (text[i] <= '['):
            vowels.append(text[i])
    return vowels