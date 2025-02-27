def return_n_greatest_chars(char_string):
    ascii_values = [ord(c) for c in char_string]
    sorted_ascii_values = sorted(set(ascii_values))[-57:]
    n_greatest_chars = [chr(i) for i in sorted_ascii_values]
    return n_greatest_chars