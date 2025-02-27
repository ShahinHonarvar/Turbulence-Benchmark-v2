def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[20:43] if char > '5' and char <= 'M' and (char in vowels)]
    return result