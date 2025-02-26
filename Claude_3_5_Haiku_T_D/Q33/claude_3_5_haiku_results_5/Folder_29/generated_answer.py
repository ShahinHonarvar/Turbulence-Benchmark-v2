def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[19:20] if char in vowels and '<' < char <= 'p']
    return result