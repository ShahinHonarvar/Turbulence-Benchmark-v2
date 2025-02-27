def return_vowels(text):
    vowels = []
    for i in range(32, 97):
        if text[i] in 'AEIOUaeiou' and text[i] > 'Q' and (text[i] <= ']'):
            vowels.append(text[i])
    return vowels