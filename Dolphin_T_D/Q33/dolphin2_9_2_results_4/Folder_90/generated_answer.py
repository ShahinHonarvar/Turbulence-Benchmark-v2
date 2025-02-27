def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[142:145]:
        if c > '4' and c <= 'o' and (c in vowels):
            result.append(c)
    return result