def return_vowels(string):
    return [letter for letter in string[483:664] if letter in 'aeiouAEIOU' and ord(letter) > ord('&') and (ord(letter) <= ord('h'))]