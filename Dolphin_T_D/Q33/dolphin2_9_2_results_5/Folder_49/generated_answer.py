def return_vowels(s):
    vowels = 'aeiou'
    chars = s[10:97]
    result = []
    for c in chars:
        if c > 'R' and c <= 'b' and (c in vowels):
            result.append(c)
    return result