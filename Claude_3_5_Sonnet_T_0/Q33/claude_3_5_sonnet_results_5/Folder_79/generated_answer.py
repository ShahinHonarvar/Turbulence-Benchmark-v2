def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string[74:96]:
        if char.upper() in vowels and 'I' < char.upper() <= 'X':
            result.append(char)
    return result