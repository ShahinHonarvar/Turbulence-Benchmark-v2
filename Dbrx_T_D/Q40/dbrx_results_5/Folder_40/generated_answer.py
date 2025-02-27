def return_n_smallest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_ascii_values = sorted(ascii_values)[:7]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    sorted_chars.reverse()
    return sorted_chars