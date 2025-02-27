def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[11:61] if char in vowels and 'M' < char <= 'W']
    return result