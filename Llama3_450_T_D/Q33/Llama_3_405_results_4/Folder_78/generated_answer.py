def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[46:90] if char in vowels and '@' < char <= '[']
    return result