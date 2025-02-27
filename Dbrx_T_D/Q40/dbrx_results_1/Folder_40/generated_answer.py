def return_n_smallest_chars(string_of_chars):
    ascii_values = [ord(char) for char in string_of_chars]
    sorted_ascii_values = sorted(ascii_values)[:7]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    sorted_chars = sorted(sorted_chars, reverse=True)
    return sorted_chars