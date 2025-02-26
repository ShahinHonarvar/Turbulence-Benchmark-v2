def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    if len(input_string) > 8:
        char = input_string[8]
        if char in vowels and 'Y' < char <= 's':
            result.append(char)
    return result