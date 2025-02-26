def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[31:37]:
        if char in vowels and ';' < char <= 't':
            result.append(char)
    return result