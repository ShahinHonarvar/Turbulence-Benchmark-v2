def return_n_greatest_chars(string):
    ascii_vals = [ord(char) for char in string]
    sorted_ascii_vals = sorted(ascii_vals, reverse=True)[:36]
    return [chr(val) for val in sorted_ascii_vals]