def return_n_smallest_chars(string):
    ascii_chars = [ord(char) for char in string]
    sorted_ascii = sorted(ascii_chars)[:35]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii][::-1]
    return sorted_chars