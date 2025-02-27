def return_vowels(string):
    return [char for char in string[71:88] if char in 'aeiouAEIOU' and ord(char) > 9 and (ord(char) <= ord('P'))]