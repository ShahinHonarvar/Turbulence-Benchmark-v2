def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 55 <= i < 65 and char in vowels and (char > 'Z') and (char <= 'w')]