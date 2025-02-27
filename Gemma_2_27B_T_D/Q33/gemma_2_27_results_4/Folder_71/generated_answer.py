def return_vowels(string):
    return [char for char in string[36:56] if char in 'aeiouAEIOU' and ord(char) > ord('+') and (ord(char) <= ord('/'))]