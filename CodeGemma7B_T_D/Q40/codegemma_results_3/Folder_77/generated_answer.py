import string

def return_n_smallest_chars(string):
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    ascii_values.sort()
    return ascii_values[:47]