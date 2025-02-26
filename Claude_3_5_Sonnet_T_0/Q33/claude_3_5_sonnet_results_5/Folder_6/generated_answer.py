def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[20:34]:
        if char.lower() in vowels and 'U' < char <= 'i':
            result.append(char)
    return result