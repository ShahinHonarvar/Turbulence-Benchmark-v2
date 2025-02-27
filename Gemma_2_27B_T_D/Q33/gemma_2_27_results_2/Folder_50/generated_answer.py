def return_vowels(string):
    return [char for char in string[11:53] if char in 'aeiouAEIOU' and ord('+') < ord(char) <= ord('W')]