def return_vowels(string):
    vowels = 'aeiou'
    result = []
    if len(string) > 8:
        char = string[8]
        if char in vowels and 'Y' < char <= 's':
            result.append(char)
    return result