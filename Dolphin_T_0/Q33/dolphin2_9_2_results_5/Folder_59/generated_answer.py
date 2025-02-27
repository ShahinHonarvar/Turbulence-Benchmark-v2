def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[8:9]:
        if 'Y' < char <= 's' and char in vowels:
            result.append(char)
    return result