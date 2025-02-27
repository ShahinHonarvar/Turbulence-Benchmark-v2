def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(set(string_of_chars))
    ascii_sorted_chars = sorted(distinct_chars, key=ord, reverse=True)
    return_n_chars = ascii_sorted_chars[:47]
    return return_n_chars