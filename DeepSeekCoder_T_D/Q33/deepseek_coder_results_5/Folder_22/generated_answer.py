def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[56:90] if c in vowels and 'K' < c <= 'z']
    return result