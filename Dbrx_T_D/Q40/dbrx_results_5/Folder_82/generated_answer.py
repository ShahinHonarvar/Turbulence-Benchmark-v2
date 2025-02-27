def return_n_smallest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list)[:60]
    return [chr(ascii) for ascii in sorted_ascii_list]