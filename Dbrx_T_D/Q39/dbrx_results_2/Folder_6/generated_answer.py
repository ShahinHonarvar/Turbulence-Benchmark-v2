def return_n_greatest_chars(input_string):
    if len(input_string) < 47:
        return sorted(list(input_string), key=ord, reverse=True)
    else:
        sorted_chars = sorted(list(input_string), key=ord, reverse=True)
        return sorted_chars[:47]