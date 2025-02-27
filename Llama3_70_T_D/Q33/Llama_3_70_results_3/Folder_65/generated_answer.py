def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s[71:88]) if char in vowels and char > '9' and (char <= 'P')]