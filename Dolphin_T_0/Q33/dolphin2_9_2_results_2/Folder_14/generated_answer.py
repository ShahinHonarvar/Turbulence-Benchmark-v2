def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[47:61] if 9 < ord(char) <= ord('O') and char in vowels]