def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    if len(input_string) > 85:
        for char in input_string[85:99]:
            if char.lower() in vowels and '/' < char <= 'n':
                result.append(char)
    return result