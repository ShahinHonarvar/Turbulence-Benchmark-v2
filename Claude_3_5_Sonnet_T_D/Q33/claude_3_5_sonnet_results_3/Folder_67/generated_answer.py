def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[21:59]:
        if char in vowels and '/' < char <= 'a':
            result.append(char)
    return result