def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[13:37] if c > 'Z' and c <= '}' and (c in vowels)]