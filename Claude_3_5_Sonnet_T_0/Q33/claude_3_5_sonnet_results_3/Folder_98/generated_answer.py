def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[3:9]:
        if char.lower() in vowels and 'S' < char <= 'U':
            result.append(char)
    return result