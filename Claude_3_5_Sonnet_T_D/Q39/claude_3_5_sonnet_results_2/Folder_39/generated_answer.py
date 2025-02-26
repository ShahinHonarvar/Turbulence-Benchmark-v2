def return_n_greatest_chars(input_string):
    return sorted(sorted(set(input_string), key=ord, reverse=True)[:23])