def return_vowels(s):
    result = []
    vowels = 'aeiou'
    for c in s[1:7]:
        if 'f' < c <= 'j' and c in vowels:
            result.append(c)
    return result