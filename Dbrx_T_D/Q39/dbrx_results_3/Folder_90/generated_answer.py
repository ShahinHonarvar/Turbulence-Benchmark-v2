def return_n_greatest_chars(input_string):
    if len(input_string) < 24:
        return sorted(list(input_string), key=ord, reverse=True)
    else:
        return sorted(list(input_string), key=ord, reverse=True)[:24]