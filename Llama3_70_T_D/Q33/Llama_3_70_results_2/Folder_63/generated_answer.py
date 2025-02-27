def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s[34:69], 34) if c > '_' and c <= 'o' and (c in vowels)]