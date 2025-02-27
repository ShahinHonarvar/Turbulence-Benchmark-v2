def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[21:23] if char in vowels and '-' < char <= 'n']
    return result