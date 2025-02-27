def return_n_greatest_chars(input_string):
    asc_input_string = sorted(list(set(input_string)))
    if len(asc_input_string) >= 60:
        return asc_input_string[-60:]
    else:
        return asc_input_string