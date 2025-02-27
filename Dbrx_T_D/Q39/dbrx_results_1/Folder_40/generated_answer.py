def return_n_greatest_chars(string):
    ascii_vals = [ord(char) for char in string if string.count(char) == 1]
    sorted_ascii_vals = sorted(ascii_vals, reverse=True)[:7]
    sorted_chars = [chr(val) for val in sorted_ascii_vals]
    return sorted_chars