def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[19:20] if char in vowels and '<' < char <= 'p']
    return result