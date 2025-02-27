def return_vowels(string):
    vowels = []
    for letter in string[74:96]:
        if letter > 'I' and letter <= 'X' and (letter in 'AEIOU'):
            vowels.append(letter)
    return vowels