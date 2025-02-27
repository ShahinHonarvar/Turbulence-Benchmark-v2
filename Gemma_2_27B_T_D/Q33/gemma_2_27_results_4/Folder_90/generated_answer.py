def return_vowels(string):
    return [char for char in string[142:145] if char in 'aeiou' and ord(char) > 4 and (ord(char) <= ord('o'))]