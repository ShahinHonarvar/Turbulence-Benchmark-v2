def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[32:97] if char in vowels and 'Q' < char <= ']']