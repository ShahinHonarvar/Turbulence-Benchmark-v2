def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    unique_ascii_values = list(set(ascii_values))
    unique_ascii_values.sort(reverse=True)
    n_greatest_ascii_values = unique_ascii_values[:87]
    n_greatest_chars = [chr(ascii_value) for ascii_value in n_greatest_ascii_values]
    return n_greatest_chars