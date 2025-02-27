def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[40:94] if char in vowels and char > '4' and (char <= 'H')]
    return result