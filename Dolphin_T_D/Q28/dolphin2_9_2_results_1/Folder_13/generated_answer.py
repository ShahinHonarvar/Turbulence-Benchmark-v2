def return_nth_smallest_ascii(string):
    ascii_vals = [ord(c) for c in string[47:81]]
    smallest_ascii_vals = sorted(ascii_vals)
    return chr(smallest_ascii_vals[3])