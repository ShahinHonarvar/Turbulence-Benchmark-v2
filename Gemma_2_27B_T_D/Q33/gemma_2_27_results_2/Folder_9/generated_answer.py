def return_vowels(string):
    return [char for char in string[13:35] if char in 'aeiouAEIOU' and ord(char) > 8 and (ord(char) <= ord('F'))]