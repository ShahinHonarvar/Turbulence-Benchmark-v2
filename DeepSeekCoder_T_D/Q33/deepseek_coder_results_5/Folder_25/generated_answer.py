def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[28:76] if c in vowels and '+' < c <= 'z']
    return result