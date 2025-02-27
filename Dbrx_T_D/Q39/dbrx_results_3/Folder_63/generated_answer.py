def return_n_greatest_chars(string_of_chars):
    ascii_values = sorted(list(map(ord, string_of_chars)))[-44:]
    result_list = []
    for ascii_val in ascii_values:
        result_list.append(chr(ascii_val))
    return result_list