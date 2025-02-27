def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[27:57] if char in vowels and 'o' < char <= 'w']