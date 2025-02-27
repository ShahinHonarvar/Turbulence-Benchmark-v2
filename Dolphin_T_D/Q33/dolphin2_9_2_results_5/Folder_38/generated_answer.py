def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[17:65]:
        if char in vowels and 'u' < char <= '{':
            result.append(char)
    return result