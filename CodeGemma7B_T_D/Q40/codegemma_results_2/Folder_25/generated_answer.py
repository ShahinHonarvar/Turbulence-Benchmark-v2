import string

def return_n_smallest_chars(input_string):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + ' '
    char_frequencies = {}
    for char in input_string:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1
    char_ascii_values = [(char, ord(char)) for char in input_string]
    char_ascii_values.sort(key=lambda x: x[1])
    return [char for char, _ in char_ascii_values[:29]]