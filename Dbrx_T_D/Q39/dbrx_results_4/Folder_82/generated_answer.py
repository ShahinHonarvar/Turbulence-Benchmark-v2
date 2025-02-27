def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in set(input_string)]
    ascii_values.sort(reverse=True)
    n_greatest_ascii_values = ascii_values[:60]
    n_greatest_chars = [chr(ascii) for ascii in n_greatest_ascii_values]
    return n_greatest_chars