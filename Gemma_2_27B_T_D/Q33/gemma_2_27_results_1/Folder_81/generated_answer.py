def return_vowels(string):
    return [char for char in string[20:43] if char in 'aeiouAEIOU' and ord(char) > 5 and (ord(char) <= ord('M'))]