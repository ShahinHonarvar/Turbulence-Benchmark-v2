def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if input_string[i] in vowels and input_string[i] > 'N' and (input_string[i] <= 'W'):
            result.append(input_string[i])
    return result