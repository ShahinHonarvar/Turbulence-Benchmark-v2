def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[1:5]:
        if char.lower() in vowels and '!' < char <= 'j':
            result.append(char)
    return result