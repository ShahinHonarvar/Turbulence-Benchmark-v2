def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[23:38]:
        if char.lower() in vowels and 'N' < char <= 'k':
            result.append(char)
    return result