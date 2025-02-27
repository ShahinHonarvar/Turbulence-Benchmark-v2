def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for c in s[40:94]:
        if c in vowels and '4' < c <= 'H':
            result.append(c)
    return result