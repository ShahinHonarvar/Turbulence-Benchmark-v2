def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for char in s[46:90] if char in vowels and '@' < char <= '[']
    return result