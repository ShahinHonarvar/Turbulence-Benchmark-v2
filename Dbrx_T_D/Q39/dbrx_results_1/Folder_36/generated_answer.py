def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list)[-32:]
    result = [chr(ascii) for ascii in sorted_ascii_list]
    return result