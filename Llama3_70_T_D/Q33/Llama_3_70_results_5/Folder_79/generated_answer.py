def return_vowels(string):
    vowels = [char for char in string[74:96] if 'I' < char <= 'X' and char in 'AEIOU']
    return vowels