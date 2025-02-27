def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[837:975]:
        if vowels.count(char) > 0 and char > 'N' and (char <= 'W'):
            result.append(char)
    return result