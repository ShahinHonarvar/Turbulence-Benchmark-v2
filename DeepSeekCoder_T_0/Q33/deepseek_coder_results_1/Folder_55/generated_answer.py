def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[1:5] if char in vowels and '!' < char <= 'j']
    return result