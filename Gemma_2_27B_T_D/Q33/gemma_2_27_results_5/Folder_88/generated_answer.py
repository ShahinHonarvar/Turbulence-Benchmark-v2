def return_vowels(string):
    return [char for char in string[70:76] if char in 'aeiouAEIOU' and ord(char) > 2 and (ord(char) <= ord(':'))]