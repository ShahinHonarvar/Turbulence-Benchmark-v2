def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[34:58] if char in vowels and 'b' < char <= 'o']
    return result