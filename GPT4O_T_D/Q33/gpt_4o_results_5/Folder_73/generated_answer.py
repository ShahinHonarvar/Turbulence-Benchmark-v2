def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[47:89] if char in vowels and '@' < char <= 'n']
    return result