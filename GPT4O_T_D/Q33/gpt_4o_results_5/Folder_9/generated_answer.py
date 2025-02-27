def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[13:35]:
        if char in vowels and '8' < char <= 'F':
            result.append(char)
    return result