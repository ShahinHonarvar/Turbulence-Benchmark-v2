def return_vowels(s):
    vowels = 'aeiou'
    specified_chars = s[43:70]
    result = [c for c in specified_chars if c > '*' and c <= 'b' and (c in vowels)]
    return result