def return_vowels(string):
    return [char for char in string[528:606] if char in 'aeiouAEIOU' and ord(char) > ord('M') and (ord(char) <= ord('X'))]