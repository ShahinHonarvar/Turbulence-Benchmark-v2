def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[60:99] if char in vowels and 'j' < char <= 'n']
    return result