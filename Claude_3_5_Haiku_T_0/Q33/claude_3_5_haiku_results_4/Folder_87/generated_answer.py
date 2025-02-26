def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[34:58] if char in vowels and 'b' < char <= 'o']
    return result