def return_vowels(s):
    vowels = 'aeiou'
    chars = s[24:68]
    result = [c for c in chars if c > 'f' and c <= '|' and (c in vowels)]
    return result