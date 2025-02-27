def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for char in input_string[483:664]:
        if char in vowels and '&' < char <= 'h':
            result.append(char)
    return result