def return_n_greatest_chars(str_of_distinct_chars):
    ordered_list = sorted(str_of_distinct_chars, key=ord, reverse=True)
    return ordered_list[:47]