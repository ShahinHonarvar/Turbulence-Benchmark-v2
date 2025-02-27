def return_vowels(string):
    vowels = []
    for letter in string[149:313]:
        if letter not in ['a', 'e', 'i', 'o', 'u'] and letter.lower() > 'm' and (letter.lower() <= 'j'):
            vowels.append(letter)
    return vowels