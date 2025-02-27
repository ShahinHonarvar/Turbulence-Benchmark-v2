def return_n_smallest_chars(s):
    ascii_vals = [ord(c) for c in s]
    sorted_ascii_vals = sorted(ascii_vals)[:76]
    return [chr(c) for c in sorted_ascii_vals]