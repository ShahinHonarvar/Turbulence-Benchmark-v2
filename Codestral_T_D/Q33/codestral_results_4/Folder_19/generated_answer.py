def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[51:77] if char in vowels and 4 < ord(char) <= ord('=')]