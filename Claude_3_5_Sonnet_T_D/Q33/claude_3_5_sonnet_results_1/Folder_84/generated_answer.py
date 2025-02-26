def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[770:852] if c.lower() in vowels and 'B' < c <= 'i']