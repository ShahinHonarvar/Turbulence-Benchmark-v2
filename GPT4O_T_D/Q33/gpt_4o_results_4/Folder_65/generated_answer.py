def return_vowels(s):
    if len(s) < 88:
        return []
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[71:88]:
        if char in vowels and '9' < char <= 'P':
            result.append(char)
    return result