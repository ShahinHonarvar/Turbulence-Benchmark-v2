def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[60:99] if c > 'j' and c <= 'n' and (c in vowels)]
    return result