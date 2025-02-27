def return_vowels(text):
    vowels = []
    for i in range(641, 872):
        if text[i] in 'aeiou' and text[i] > '>' and (text[i] <= 'q'):
            vowels.append(text[i])
    return vowels