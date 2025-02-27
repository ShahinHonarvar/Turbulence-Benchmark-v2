def return_vowels(string):
    vowels = 'aeiou'
    range_chars = string[149:313]
    result = []
    for char in range_chars:
        if char > 'M' and char <= 'j':
            if char in vowels:
                result.append(char)
    return result