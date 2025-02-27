def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[29:31]:
        if char in vowels and char > 'a' and (char <= 'f'):
            result.append(char)
    return result