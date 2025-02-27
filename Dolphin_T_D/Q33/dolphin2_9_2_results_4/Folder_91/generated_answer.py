def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[4:8] if c in vowels and c > 'p' and (c <= 'r')]