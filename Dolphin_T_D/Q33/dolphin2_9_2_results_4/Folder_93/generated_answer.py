def return_vowels(s):
    vowels = 'aeiou'
    chars = s[54:82]
    result = [c for c in chars if c > '=' and c <= '@' and (c in vowels)]
    return result