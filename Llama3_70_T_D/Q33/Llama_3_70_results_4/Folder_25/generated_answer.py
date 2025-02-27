def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[28:77]:
        if char > '+' and char <= 'z' and (char in vowels):
            result.append(char)
    return result