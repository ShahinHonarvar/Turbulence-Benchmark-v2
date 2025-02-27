def return_n_smallest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_ascii_values = sorted(ascii_values)[:57]
    chars = [chr(char) for char in sorted_ascii_values]
    return chars