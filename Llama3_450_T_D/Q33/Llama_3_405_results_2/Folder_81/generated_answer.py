def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[20:43] if c in vowels and '5' < c <= 'M']
    return result