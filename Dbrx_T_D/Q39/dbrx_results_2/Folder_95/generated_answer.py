def return_n_greatest_chars(input_string):
    if len(input_string) < 36:
        return sorted(input_string, key=ord, reverse=True)
    else:
        return sorted(input_string, key=ord, reverse=True)[:36]