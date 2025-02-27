def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[50:77]:
        if char > 'l' and char <= 'r' and (char in vowels):
            result.append(char)
    return result