from functools import cmp_to_key

def return_n_smallest_chars(text):
    char_ascii_values = [(char, ord(char)) for char in text]
    char_ascii_values.sort(key=cmp_to_key(lambda x, y: x[1] - y[1]))
    return char_ascii_values[:26]