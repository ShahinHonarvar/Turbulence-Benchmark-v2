def return_n_greatest_chars(input_string):
    sorted_list = sorted(input_string, reverse=True)[:83]
    sorted_list.sort()
    return sorted_list