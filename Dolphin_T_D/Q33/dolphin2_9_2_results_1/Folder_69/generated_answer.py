def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(641, 872):
        if input_string[index] > '>' and input_string[index] <= 'q':
            if input_string[index] in vowels:
                result.append(input_string[index])
    return result