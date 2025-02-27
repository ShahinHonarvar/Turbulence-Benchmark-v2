def return_n_greatest_chars(string_of_chars):
    ascii_list = [ord(char) for char in string_of_chars]
    sorted_ascii_list = sorted(ascii_list, reverse=True)[:84]
    result_list = [chr(ascii) for ascii in sorted_ascii_list]
    return result_list