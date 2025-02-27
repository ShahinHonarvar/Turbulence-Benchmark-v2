def return_vowels(text):
    vowels = []
    for i in range(max(142, len(text))):
        if i < 145 and text[i] in 'aeiou' and (text[i] > 'd') and (text[i] <= 'o'):
            vowels.append(text[i])
    return vowels