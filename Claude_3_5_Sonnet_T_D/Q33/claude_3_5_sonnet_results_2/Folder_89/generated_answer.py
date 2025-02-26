def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    if len(input_string) > 50:
        char = input_string[50]
        if char in vowels and ',' < char <= 'v':
            result.append(char)
    return result