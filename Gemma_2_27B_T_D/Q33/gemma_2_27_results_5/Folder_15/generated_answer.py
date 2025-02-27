def return_vowels(string):
    return [char for char in string[5:6] if char in 'aeiouAEIOU' and ord(char) > ord('3') and (ord(char) <= ord('^'))]