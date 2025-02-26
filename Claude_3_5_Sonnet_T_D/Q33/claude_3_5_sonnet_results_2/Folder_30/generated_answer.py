def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string[11:61]:
        if char.upper() in vowels and 'M' < char.upper() <= 'W':
            result.append(char)
    return result