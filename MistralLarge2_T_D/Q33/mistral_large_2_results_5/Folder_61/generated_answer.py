def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[1:4] if char in vowels and 'c' < char <= 'i']