def return_n_smallest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort()
    min_chars = [char for char in input_string if ord(char) in ascii_list[:20]]
    min_chars.sort(reverse=True)
    return min_chars