def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[32:97] if c > 'Q' and c <= ']' and (c in vowels)]