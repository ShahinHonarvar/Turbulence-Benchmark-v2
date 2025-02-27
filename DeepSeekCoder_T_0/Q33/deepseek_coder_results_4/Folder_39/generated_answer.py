def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[32:97] if char in vowels and 'Q' < char <= ']']
    return result