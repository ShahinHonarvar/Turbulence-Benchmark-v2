def return_vowels(s):
    vowels = 'aeiou'
    char_range = s[85:99]
    result = [c for c in char_range if c > '/' and c <= 'n' and (c in vowels)]
    return result