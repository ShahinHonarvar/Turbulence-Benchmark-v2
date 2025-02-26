def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[46:49]:
        if char in vowels and '[' < char <= 'p':
            result.append(char)
    return result