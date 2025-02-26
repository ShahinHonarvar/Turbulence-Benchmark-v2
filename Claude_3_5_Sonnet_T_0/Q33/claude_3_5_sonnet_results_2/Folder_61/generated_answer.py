def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[1:4]:
        if char.lower() in vowels and 'C' < char <= 'I':
            result.append(char)
    return result