def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s if char in vowels and 'P' < char <= 'z' and (64 <= ord(char) < 82)]
    return result