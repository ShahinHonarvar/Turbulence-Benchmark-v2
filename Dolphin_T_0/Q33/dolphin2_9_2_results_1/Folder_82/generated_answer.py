def return_vowels(s):
    result = []
    vowels = 'aeiou'
    for char in s[86:99]:
        if 'E' < char <= 'r' and char in vowels:
            result.append(char)
    return result