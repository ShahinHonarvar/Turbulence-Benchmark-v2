def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[46:49] if char in vowels and '[' < char <= 'p']
    return result