def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[1:5] if char in vowels and '!' < char <= 'j']