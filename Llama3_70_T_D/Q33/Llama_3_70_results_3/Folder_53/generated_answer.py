def return_vowels(s):
    vowels = 'aeiou'
    return [char for i, char in enumerate(s) if 27 <= i < 57 and char in vowels and (char > 'o') and (char <= 'w')]