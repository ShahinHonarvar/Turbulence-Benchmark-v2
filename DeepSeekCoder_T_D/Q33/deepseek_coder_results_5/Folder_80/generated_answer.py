def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[85:99] if char in vowels and '/' < char <= 'n']
    return result