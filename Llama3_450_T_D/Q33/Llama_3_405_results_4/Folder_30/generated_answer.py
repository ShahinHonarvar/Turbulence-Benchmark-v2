def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[11:61] if c in vowels and 'M' < c <= 'W']
    return result