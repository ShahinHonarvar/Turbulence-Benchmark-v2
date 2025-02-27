def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[77:84] if char in vowels and '(' < char <= 'G']
    return result