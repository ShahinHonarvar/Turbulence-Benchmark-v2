def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_list = []
    for char in input_string[56:90]:
        if char > 'K' and char <= 'z' and (char in vowels):
            output_list.append(char)
    return output_list