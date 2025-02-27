def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[14:60] if char in vowels and 'D' < char <= 'v']