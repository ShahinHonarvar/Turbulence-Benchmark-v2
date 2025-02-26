def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[273:275]:
        if char in vowels and '+' < char <= 'o':
            result.append(char)
    return result