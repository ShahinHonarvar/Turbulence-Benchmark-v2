def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[63:79] if char in vowels and 'D' < char <= 'y']
    return result