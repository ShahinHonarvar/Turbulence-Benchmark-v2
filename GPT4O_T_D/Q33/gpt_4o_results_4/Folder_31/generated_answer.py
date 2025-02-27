def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[65:70] if char in vowels and '%' < char <= 'G']
    return result