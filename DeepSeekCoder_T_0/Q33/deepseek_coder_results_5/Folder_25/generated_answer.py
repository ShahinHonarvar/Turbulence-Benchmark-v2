def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[28:76] if c > '+' and c <= 'z' and (c in vowels)]
    return result