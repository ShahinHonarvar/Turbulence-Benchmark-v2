def return_n_smallest_chars(s):
    ascii_vals = [ord(c) for c in s]
    sorted_ascii_vals = sorted(ascii_vals)[:11]
    return [chr(i) for i in sorted(sorted_ascii_vals, reverse=True)]