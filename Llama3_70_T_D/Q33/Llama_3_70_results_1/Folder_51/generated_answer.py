def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s[56:68]) if char in vowels and char > 'M' and (char <= 'X')]