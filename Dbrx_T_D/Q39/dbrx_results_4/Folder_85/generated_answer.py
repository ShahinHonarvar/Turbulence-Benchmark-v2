def return_n_greatest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values, reverse=True)[:85]
    sorted_chars = [chr(c) for c in sorted_ascii_values]
    return sorted_chars