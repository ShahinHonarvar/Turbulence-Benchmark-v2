def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[1:7]:
        if char.lower() in vowels and 'F' < char <= 'j':
            result.append(char)
    return result