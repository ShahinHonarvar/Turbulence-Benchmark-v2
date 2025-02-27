def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[56:96]:
        if char in vowels and '&' < char <= 'T':
            result.append(char)
    return result