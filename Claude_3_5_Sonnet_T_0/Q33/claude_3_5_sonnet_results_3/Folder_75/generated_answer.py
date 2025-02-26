def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string[20:41]:
        if char.upper() in vowels and 'K' < char.upper() <= 'Z':
            result.append(char)
    return result