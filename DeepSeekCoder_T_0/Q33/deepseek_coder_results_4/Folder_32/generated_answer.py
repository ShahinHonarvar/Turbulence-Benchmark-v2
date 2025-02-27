def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[45:76] if c in vowels and 'b' < c <= 'z']
    return result