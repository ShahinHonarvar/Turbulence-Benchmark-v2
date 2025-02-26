def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[4:8]:
        if char.lower() in vowels and 'P' < char <= 'r':
            result.append(char)
    return result