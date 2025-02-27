def return_n_smallest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)[:52]
    sorted_chars = [chr(i) for i in sorted_ascii_values]
    return sorted_chars