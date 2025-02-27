def return_n_smallest_chars(input_string):
    list_of_chars = sorted(list(input_string), key=lambda x: ord(x))
    return list_of_chars[:49]