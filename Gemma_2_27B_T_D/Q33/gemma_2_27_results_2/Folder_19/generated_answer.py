def return_vowels(string):
    return [char for char in string[51:77] if char in 'aeiouAEIOU' and 4 < ord(char) <= ord('=')]