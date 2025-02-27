def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list, reverse=True)
    n_greatest_chars = [chr(ascii) for ascii in sorted_ascii_list[:16]]
    return n_greatest_chars