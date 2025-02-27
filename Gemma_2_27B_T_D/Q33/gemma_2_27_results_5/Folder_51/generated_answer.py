def return_vowels(string):
    return [char for char in string[56:68] if char in 'AEIOU' and ord(char) > ord('M') and (ord(char) <= ord('X'))]