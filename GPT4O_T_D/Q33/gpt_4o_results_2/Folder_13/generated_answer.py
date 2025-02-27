def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return [char for char in input_string[149:313] if char in vowels and 'M' < char <= 'j']