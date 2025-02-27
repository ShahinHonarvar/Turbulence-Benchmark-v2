def return_vowels(string):
    return [char for char in string[21:23] if char in 'aeiouAEIOU' and ord('-') < ord(char) <= ord('n')]