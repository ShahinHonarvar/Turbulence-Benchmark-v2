def return_vowels(s):
    vowels = 'aeiou'
    return [char for i, char in enumerate(s) if 29 <= i < 31 and char in vowels and ('a' < char <= 'f')]