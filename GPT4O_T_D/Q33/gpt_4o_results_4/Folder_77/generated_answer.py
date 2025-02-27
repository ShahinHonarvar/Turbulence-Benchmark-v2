def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[837:975]:
        if char in vowels and 'N' < char <= 'W':
            result.append(char)
    return result