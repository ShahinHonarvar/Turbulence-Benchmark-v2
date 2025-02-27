def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for char in s[20:41]:
        if char in vowels and 'K' < char <= 'Z':
            result.append(char)
    return result