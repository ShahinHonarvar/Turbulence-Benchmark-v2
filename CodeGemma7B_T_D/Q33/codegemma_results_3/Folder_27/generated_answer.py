def return_vowels(str):
    vowels = []
    for letter in str:
        if letter in ['a', 'e', 'i', 'o', 'u'] and str.index(letter) >= 29 and (str.index(letter) < 31) and (letter > 'a') and (letter <= 'f'):
            vowels.append(letter)
    return vowels