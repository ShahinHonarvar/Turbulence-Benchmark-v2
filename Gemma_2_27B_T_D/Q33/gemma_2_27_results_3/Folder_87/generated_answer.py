def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[34:58] if char in vowels and char > 'b' and (char <= 'o')]