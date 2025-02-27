def return_vowels(s):
    result = []
    vowels = 'aeiou'
    for char in s[8:9]:
        if char > 'Y' and char <= 's' and (char in vowels):
            result.append(char)
    return result