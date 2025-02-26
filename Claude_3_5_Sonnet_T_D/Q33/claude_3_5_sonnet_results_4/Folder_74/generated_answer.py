def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[69:82]:
        if char in vowels and '[' < char <= '~':
            result.append(char)
    return result