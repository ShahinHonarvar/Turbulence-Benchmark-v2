def return_vowels(s):
    vowels = 'AEIOU'
    return [char for char in s[11:61] if char.upper() in vowels and 'M' < char.upper() <= 'W']