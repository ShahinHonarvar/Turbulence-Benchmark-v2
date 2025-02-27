def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[70:76]:
        if 'a' <= char <= ':' and char > '2':
            if char in vowels:
                result.append(char)
    return result