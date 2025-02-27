def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[15:86]:
        if '@' < c <= '~' and c in vowels:
            result.append(c)
    return result