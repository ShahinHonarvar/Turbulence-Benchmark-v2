def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for char in string[1:9]:
        if char.lower() in vowels and '?' < char <= 'k':
            result.append(char)
    return result