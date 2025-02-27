def return_nth_smallest_ascii(input_str):
    relevant_chars = input_str[29:34]
    ascii_vals = [ord(char) for char in relevant_chars]
    sorted_ascii_vals = sorted(ascii_vals)
    return chr(sorted_ascii_vals[4])