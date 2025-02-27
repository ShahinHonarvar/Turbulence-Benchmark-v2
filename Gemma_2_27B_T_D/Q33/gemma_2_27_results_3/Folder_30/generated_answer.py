def return_vowels(string):
    return [char for char in string[11:61] if char in 'EOIU' and ord('M') < ord(char) <= ord('W')]