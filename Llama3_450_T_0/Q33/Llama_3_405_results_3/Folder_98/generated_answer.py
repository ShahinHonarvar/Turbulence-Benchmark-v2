def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for char in s[3:9] if char in vowels and 'S' < char <= 'U']