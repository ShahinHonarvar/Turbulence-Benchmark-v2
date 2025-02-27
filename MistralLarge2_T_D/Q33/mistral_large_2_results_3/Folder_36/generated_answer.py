def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[604:949] if char in vowels and 'N' < char <= 'U']
    return result