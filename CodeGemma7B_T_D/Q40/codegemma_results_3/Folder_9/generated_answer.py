from functools import cmp_to_key

def return_n_smallest_chars(string):
    char_values = [(char, ord(char)) for char in string]
    char_values.sort(key=lambda x: x[1])
    return [char for char, _ in char_values[:20]]