def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[17:65] if char in vowels and 'U' < char <= '{']
    return result