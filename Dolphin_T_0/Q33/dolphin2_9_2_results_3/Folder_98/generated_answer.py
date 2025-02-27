def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = [input_string[i] for i in range(3, 9) if input_string[i] in vowels and 's' < input_string[i] <= 'u']
    return output