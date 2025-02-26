def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string[24:59]:
        if char.upper() in vowels and 'N' < char.upper() <= 'U':
            result.append(char)
    return result