def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for c in s[19:32]:
        if 0 < ord(c) <= 7 and c in vowels:
            result.append(c)
    return result