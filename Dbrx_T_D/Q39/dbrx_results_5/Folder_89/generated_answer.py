def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list)[-55:]
    return [chr(ascii) for ascii in sorted_ascii_list]