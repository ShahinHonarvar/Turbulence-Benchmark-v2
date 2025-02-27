def return_vowels(s):
    vowels = 'AEIOUaeiou'
    specified_vowels = [c for c in s[82:90] if c in vowels and 'T' < c <= 'b']
    return specified_vowels