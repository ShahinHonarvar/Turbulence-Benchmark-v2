def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[5:6]:
        if c in vowels and '3' < c <= '^':
            result.append(c)
    return result