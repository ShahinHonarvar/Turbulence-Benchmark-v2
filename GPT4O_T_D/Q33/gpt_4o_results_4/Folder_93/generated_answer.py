def return_vowels(s):
    if len(s) < 54:
        return []
    vowels = 'AEIOU'
    result = []
    for char in s[54:82]:
        if '=' < char <= '@' and char in vowels:
            result.append(char)
    return result