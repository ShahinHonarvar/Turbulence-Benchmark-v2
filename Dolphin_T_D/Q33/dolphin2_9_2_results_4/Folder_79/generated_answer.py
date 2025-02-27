def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [input_string[i] for i in range(74, 96) if input_string[i] in vowels and input_string[i] > 'I' and (input_string[i] <= 'X')]
    return result