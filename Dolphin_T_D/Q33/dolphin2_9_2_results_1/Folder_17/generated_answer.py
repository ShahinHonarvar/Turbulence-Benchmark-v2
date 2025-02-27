def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[60:99]:
        if char > 'j' and char <= 'n':
            if char in vowels:
                result.append(char)
    return result