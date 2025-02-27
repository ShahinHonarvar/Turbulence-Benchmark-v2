def return_n_greatest_chars(input_string):
    sorted_list = sorted(input_string, key=lambda x: x, reverse=True)[:68]
    return sorted(sorted_list)