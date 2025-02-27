def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[69:82] if char in vowels and ']' < char <= '~']