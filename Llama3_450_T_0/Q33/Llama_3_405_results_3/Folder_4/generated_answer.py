def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[40:91] if char in vowels and 'A' < char <= 'x']
    return result