def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[1:9]:
        if char.lower() in vowels and '?' < char <= 'k':
            result.append(char)
    return result