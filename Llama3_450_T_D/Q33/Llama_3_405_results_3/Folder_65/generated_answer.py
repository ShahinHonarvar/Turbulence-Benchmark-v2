def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s) if 71 <= i < 88 and char > '9' and (char <= 'P') and (char in vowels)]
    return result