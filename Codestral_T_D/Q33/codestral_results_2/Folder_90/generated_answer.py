def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[142:145] if char in vowels and 4 < ord(char) <= ord('o')]