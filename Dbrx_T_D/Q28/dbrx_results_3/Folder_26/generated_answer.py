def return_nth_smallest_ascii(input_str):
    ascii_vals = [ord(c) for c in input_str if input_str.index(c) in range(1, 37)]
    ascii_vals.sort()
    return chr(ascii_vals[14])