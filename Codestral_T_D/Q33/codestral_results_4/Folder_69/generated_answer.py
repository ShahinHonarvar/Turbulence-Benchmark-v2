def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[641:872] if char in vowels and '>' < char <= 'q']