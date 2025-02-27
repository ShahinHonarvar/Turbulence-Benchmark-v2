def return_vowels(text):
    vowels = []
    for i in range(20, 41):
        if i in range(len(text)):
            if text[i] in 'AEIOUaeiou' and text[i] > 'K' and (text[i] <= 'Z'):
                vowels.append(text[i])
    return vowels