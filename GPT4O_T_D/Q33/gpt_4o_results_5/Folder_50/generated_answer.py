def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[11:53] if char in vowels and '+' < char <= 'W']
    return result