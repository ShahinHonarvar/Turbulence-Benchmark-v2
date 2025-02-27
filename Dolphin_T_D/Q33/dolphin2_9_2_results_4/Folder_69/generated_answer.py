def return_vowels(string):
    result = []
    vowels = 'aeiou'
    for char in string[641:872]:
        if '!' <= char <= 'q':
            if char in vowels:
                result.append(char)
    return result