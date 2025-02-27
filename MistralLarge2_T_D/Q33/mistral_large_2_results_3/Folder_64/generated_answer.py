def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[1:7] if char in vowels and 'F' < char <= 'j']