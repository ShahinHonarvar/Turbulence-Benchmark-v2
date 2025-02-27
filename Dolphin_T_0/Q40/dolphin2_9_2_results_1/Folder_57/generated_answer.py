def return_n_smallest_chars(input_string):
    input_string_list = list(input_string)
    sorted_list = sorted(input_string_list, key=lambda c: ord(c))
    return sorted(sorted_list[:29], reverse=True)