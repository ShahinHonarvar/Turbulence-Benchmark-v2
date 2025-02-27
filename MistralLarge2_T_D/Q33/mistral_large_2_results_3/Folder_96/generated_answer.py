def return_vowels(string):
    vowels = 'AEIOUaeiou'
    return [char for char in string[77:84] if char in vowels and ord(char) > ord('(') and (ord(char) <= ord('G'))]