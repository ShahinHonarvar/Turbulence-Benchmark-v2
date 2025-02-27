def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 34 <= i < 69 and char in vowels and ('_' < char <= 'o')]
    return result