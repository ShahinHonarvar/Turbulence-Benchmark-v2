def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    smallest_75 = sorted_chars[:75]
    return sorted(smallest_75, reverse=True)