def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[50:77]:
        if char > '&' and char <= 'r':
            if char in vowels:
                result.append(char)
    return result