def return_n_smallest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)[:36]
    sorted_chars = [chr(c) for c in sorted_ascii_values]
    sorted_chars.reverse()
    return sorted_chars