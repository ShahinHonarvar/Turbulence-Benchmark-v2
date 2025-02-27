def return_vowels(s):
    vowels = 'AEIOUaeiou'
    s = s[74:96]
    return [char for char in s if char in vowels and char > 'I' and (char <= 'X')]