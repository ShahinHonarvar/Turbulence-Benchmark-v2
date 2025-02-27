def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    unique_ascii_values = list(set(ascii_values))
    unique_ascii_values.sort(reverse=True)
    top_87_values = unique_ascii_values[:87]
    result = [chr(value) for value in top_87_values]
    return result