def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for c in string[21:59]:
        if '/' < c <= 'a' and c in vowels:
            result.append(c)
    return result