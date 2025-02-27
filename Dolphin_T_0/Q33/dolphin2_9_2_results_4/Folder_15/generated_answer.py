def return_vowels(s):
    vowels = 'aeiou'
    substring = s[5:6]
    filtered = [c for c in substring if c in vowels]
    return filtered