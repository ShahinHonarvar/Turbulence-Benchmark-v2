def return_vowels(text):
    vowels = []
    for i in range(19, 32):
        if text[i].lower() in 'aeiou' and text[i] > '0' and (text[i] <= '7'):
            vowels.append(text[i])
    return vowels