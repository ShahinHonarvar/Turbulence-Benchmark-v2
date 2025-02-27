def return_n_greatest_chars(string_of_chars):
    ascii_list = [ord(char) for char in set(string_of_chars)]
    ascii_list.sort()
    result_list = []
    for ascii_value in ascii_list[-80:]:
        result_list.append(chr(ascii_value))
    return result_list