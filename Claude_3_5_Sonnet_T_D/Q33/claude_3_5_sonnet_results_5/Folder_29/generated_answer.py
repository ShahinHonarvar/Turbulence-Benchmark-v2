def return_vowels(string):
    vowels = 'aeiou'
    result = []
    if len(string) > 19:
        for char in string[19:20]:
            if char in vowels and '<' < char <= 'p':
                result.append(char)
    return result