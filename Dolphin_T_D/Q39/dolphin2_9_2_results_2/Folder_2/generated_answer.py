def return_n_greatest_chars(input_string):
    available_chars = list(input_string)
    sorted_chars = sorted(available_chars, key=lambda x: ord(x), reverse=True)
    return_list = sorted_chars[:48]
    return_list.sort()
    return return_list