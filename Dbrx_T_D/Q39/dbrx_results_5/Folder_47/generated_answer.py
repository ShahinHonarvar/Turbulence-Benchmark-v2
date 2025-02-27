def return_n_greatest_chars(input_string):
    ascii_values = list(map(ord, input_string))
    unique_ascii_values = list(set(ascii_values))
    unique_ascii_values.sort(reverse=True)
    return [chr(i) for i in unique_ascii_values[:21]]