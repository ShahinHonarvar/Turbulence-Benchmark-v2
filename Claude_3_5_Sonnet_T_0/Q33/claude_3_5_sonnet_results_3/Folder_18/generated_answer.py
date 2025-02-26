def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string[528:606]:
        if char.upper() in vowels and 'M' < char.upper() <= 'X':
            result.append(char)
    return result