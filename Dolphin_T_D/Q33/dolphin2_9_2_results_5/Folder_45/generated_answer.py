def return_vowels(s):
    vowels = 'aeiou'
    range_chars = s[43:70]
    return [c for c in range_chars if c in vowels and '*' < c <= 'b']