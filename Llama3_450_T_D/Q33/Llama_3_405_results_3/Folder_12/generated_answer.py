def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[13:37] if char in vowels and 'Z' < char <= '}']
    return result