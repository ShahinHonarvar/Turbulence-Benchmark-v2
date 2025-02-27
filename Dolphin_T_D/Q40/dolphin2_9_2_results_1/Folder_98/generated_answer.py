def return_n_smallest_chars(string):
    ascii_vals = [ord(c) for c in string]
    sorted_chars = [c for _, c in sorted(zip(ascii_vals, string))]
    return sorted_chars[:68]