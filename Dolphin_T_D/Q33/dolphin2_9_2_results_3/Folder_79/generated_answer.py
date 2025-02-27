def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[74:96]:
        if 'I' < char <= 'X' and char in vowels:
            result.append(char)
    return result