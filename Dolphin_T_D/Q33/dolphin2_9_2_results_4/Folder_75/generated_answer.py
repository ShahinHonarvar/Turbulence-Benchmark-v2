def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[20:41]:
        if 'K' < c <= 'Z' and c in vowels:
            result.append(c)
    return result