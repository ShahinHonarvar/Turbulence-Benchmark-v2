def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[21:23]:
        if char.lower() in vowels and '-' < char <= 'n':
            result.append(char)
    return result