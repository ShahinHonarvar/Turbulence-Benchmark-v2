def return_n_greatest_chars(string):
    ascii_vals = [ord(char) for char in string]
    sorted_ascii_vals = sorted(ascii_vals)[-76:]
    result = [chr(val) for val in sorted_ascii_vals]
    return result