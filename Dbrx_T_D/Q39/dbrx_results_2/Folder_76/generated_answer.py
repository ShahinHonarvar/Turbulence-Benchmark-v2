def return_n_greatest_chars(string_of_chars):
    ascii_vals = [ord(char) for char in string_of_chars]
    sorted_ascii_vals = sorted(ascii_vals, reverse=True)[:3]
    sorted_chars = [chr(char) for char in sorted_ascii_vals]
    return sorted_chars