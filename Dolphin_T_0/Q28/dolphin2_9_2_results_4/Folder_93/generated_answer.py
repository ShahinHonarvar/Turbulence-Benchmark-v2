def return_nth_smallest_ascii(input_str):
    chars = input_str[42:60]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chr(ascii_vals[16])