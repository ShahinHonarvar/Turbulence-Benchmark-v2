def return_n_smallest_chars(given_string):
    ascii_values_list = [ord(char) for char in given_string]
    sorted_ascii_values_list = sorted(ascii_values_list)[:84]
    return [chr(ascii) for ascii in sorted_ascii_values_list]