def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[34:58] if char > 'b' and char <= 'o' and (char in vowels)]