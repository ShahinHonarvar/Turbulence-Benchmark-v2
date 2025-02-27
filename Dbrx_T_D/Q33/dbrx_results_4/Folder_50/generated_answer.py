def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    input_length = len(input_string)
    for i in range(11, min(53, input_length)):
        char = input_string[i]
        if char > '+' and char <= 'W' and (char in vowels):
            result.append(char)
    return result