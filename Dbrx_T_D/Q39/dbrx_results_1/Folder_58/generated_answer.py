def return_n_greatest_chars(string_):
    sorted_chars = sorted(set(string_), key=ord, reverse=True)[:49]
    return sorted_chars