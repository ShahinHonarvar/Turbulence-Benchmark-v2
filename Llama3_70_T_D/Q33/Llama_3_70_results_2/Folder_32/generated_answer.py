def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[45:76] if c > 'b' and c <= 'z' and (c in vowels)]
    return result