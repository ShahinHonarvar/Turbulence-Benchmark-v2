def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[29:31] if char in vowels and 'a' < char <= 'f']
    return result