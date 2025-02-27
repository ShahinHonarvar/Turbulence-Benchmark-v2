def return_n_smallest_chars(string_of_chars):
    ascii_list = [ord(char) for char in string_of_chars]
    sorted_list = sorted(ascii_list)[:52]
    result = [chr(ascii) for ascii in sorted_list]
    return result[::-1]