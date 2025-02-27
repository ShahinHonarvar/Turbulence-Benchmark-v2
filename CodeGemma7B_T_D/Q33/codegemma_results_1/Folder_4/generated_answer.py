def return_vowels(text):
    vowels = []
    for letter in text[40:91]:
        if letter in set('aeiouAEIOU') and letter > 'A' and (letter <= 'x'):
            vowels.append(letter)
    return vowels