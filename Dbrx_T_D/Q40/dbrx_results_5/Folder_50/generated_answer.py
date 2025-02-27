def return_n_smallest_chars(s):
    ascii_list = [ord(char) for char in s]
    sorted_ascii_list = sorted(ascii_list)[:16]
    sorted_ascii_list.reverse()
    return [chr(asc) for asc in sorted_ascii_list]