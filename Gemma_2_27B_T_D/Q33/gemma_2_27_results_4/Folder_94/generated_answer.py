def return_vowels(string):
    return [char for char in string[40:94] if char in 'aeiouAEIOU' and 4 < ord(char) <= ord('H')]