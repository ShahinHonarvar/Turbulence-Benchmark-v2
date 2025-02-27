def return_nth_smallest_ascii(input_str):
    ascii_vals = [ord(char) for char in input_str if 22 <= input_str.index(char) <= 74]
    ascii_vals.sort()
    return chr(ascii_vals[11]) if len(ascii_vals) > 12 else None