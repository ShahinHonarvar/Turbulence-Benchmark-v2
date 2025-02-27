def return_n_greatest_chars(input_string):
    if not isinstance(input_string, str) or not input_string:
        return []
    input_list = sorted(list(input_string), reverse=True)[:61]
    return input_list