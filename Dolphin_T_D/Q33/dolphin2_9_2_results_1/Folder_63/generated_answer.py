def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[34:69]:
        if c > '_' and c <= 'o' and (c in vowels):
            result.append(c)
    return result