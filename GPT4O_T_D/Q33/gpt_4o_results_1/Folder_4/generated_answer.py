def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[40:91] if char in vowels and 'A' < char <= 'x']