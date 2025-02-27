def return_vowels(string):
    return [char for char in string[40:94] if char in 'aeiouAEIOU' and ord(char) > 4 and (ord(char) <= ord('H'))]