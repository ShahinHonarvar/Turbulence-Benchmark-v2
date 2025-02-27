def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if i < len(input_string) and input_string[i] in vowels and (input_string[i] > 'B') and (input_string[i] <= 'i'):
            result.append(input_string[i])
    return result