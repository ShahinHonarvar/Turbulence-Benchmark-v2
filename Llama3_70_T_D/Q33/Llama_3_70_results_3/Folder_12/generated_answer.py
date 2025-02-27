def return_vowels(s):
    vowels = 'AEIOU'
    return [c for i, c in enumerate(s[13:37]) if c in vowels and c > 'Z' and (c <= '}')]