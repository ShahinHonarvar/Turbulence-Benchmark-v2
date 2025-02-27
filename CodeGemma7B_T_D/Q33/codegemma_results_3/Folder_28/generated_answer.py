def return_vowels(string):
    vowels = [letter for letter in string[41:50] if letter in 'AEIOUaeiou' and letter > 'W' and (letter <= '[')]
    return vowels