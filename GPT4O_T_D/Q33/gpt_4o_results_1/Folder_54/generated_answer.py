def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[23:85]:
        if char in vowels and 'W' < char <= 'v':
            result.append(char)
    return result