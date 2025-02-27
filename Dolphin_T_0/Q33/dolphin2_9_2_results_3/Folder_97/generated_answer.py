def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[328:455]:
        if char > '<' and char <= 'z' and (char in vowels):
            result.append(char)
    return result