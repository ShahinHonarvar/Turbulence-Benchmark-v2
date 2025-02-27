def return_vowels(str1):
    vowels = []
    for idx, letter in enumerate(str1[149:313]):
        if letter.isalpha() and letter.lower() not in vowels and (letter > 'M') and (letter <= 'j'):
            vowels.append(letter.lower())
    return vowels