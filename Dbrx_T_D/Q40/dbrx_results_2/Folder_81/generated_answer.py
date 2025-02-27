def return_n_smallest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)[:64]
    result = [chr(v) for v in sorted_ascii_values]
    return result