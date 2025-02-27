def return_vowels(s):
    vowels = 'aeiou'
    r = []
    for c in s[32:97]:
        if 'Q' < c <= ']':
            if c in vowels:
                r.append(c)
    return r