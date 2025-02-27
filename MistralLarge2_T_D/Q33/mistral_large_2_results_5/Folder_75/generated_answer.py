def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[20:41] if char > 'K' and char <= 'Z' and (char in vowels)]