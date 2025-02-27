def return_vowels(s):
    vowels = 'aeiou'
    result = [char for i, char in enumerate(s) if 85 <= i < 99 and char > '/' and (char <= 'n') and (char in vowels)]
    return result