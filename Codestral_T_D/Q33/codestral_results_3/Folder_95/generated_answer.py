def return_vowels(string):
    vowels = [char for char in string[32:61] if 'a' <= char <= 'p' and char in 'aeiou']
    return vowels