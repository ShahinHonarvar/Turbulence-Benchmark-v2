def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(74, 96):
        char = chr(i)
        if char in s and char > 'I' and (char <= 'X') and (char in vowels):
            result.append(char)
    return result