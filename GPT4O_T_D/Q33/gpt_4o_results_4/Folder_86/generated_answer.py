def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for char in input_string[273:275]:
        if char in vowels and '+' < char <= 'o':
            result.append(char)
    return result