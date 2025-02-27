def return_n_smallest_chars(input_str):
    ascii_list = [ord(char) for char in input_str]
    ascii_list.sort()
    n_smallest_chars = [chr(ascii_list[i]) for i in range(9)]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars