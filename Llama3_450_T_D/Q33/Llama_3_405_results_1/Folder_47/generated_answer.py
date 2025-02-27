def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[23:38] if c in vowels and 'N' < c <= 'k']
    return result