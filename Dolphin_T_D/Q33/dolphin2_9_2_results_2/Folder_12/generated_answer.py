def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[13:37] if c > 'Z' and c <= '}' and (c in vowels)]