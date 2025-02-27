def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for c in s[24:59]:
        if c > 'N' and c <= 'U' and (c in vowels):
            result.append(c)
    return result