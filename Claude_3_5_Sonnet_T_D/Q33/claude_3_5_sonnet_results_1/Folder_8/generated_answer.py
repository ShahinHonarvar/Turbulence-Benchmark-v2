def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[64:82] if c.lower() in vowels and 'P' < c <= 'z']