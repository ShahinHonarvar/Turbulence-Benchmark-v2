def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(set(string_of_chars))
    return sorted(distinct_chars, key=ord)[:48]