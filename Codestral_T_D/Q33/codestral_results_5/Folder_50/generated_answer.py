def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[11:53] if char in vowels and '+' < char <= 'W']