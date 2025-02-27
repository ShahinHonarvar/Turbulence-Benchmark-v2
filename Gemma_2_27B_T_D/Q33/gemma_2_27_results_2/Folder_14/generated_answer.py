def return_vowels(string):
    return [char for char in string[47:61] if char in 'aeiouAEIOU' and 9 < ord(char) <= ord('O')]