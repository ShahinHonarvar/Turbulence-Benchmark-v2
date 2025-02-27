def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s[260:322]) if char in vowels and '%' < char <= 'U']
    return result