def return_vowels(s):
    vowels = 'aeiou'
    return [char for i, char in enumerate(s) if 34 <= i < 69 and char > '_' and (char <= 'o') and (char in vowels)]