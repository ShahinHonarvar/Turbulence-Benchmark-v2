def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for char in s[20:41]:
        if char > 'K' and char <= 'Z' and (char in vowels):
            result.append(char)
    return result