def return_n_smallest_chars(input_string):
    ascii_list = []
    for char in input_string:
        ascii_list.append(ord(char))
    sorted_ascii_list = sorted(ascii_list)[:72]
    sorted_ascii_list.reverse()
    result_string = ''
    for ascii_value in sorted_ascii_list:
        result_string += chr(ascii_value)
    return result_string