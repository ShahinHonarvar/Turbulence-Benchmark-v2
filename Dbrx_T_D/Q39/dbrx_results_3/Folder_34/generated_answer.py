def return_n_greatest_chars(input_string):
    if len(input_string) < 9:
        return sorted(list(input_string), reverse=True)
    else:
        return sorted(list(set(input_string)), reverse=True)[:9]