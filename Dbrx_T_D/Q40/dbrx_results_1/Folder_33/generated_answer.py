def return_n_smallest_chars(s):
    ascii_list = [ord(char) for char in s]
    sorted_ascii_list = sorted(ascii_list)[:36]
    sorted_ascii_list.reverse()
    return [chr(ascii) for ascii in sorted_ascii_list]