def return_vowels(s):
    vowels = 'AEIOU'
    s = s[11:61]
    result = [char for char in s if char in vowels and 'M' < char <= 'W']
    return result