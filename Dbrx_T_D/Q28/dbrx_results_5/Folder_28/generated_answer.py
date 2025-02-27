def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string[25:78] if 25 <= input_string.index(char) <= 77]
    ascii_list.sort()
    return ascii_list[15]