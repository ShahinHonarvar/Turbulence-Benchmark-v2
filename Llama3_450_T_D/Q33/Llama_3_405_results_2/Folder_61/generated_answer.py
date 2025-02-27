def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[1:4] if c in vowels and 'C' < c <= 'I']
    return result