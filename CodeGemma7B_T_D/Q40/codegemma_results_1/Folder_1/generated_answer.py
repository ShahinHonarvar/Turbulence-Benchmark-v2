def return_n_smallest_chars(given_str):
    ascii_values = [(char, ord(char)) for char in given_str]
    ascii_values.sort(key=lambda x: x[1])
    return ascii_values[:11][::-1]