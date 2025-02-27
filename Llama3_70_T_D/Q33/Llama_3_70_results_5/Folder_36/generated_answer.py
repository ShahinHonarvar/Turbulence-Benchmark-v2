def return_vowels(string):
    vowels = 'AEIOUaeiou'
    result = []
    for char in string[604:949]:
        if char in vowels and 'N' < char <= 'U':
            result.append(char)
    return result