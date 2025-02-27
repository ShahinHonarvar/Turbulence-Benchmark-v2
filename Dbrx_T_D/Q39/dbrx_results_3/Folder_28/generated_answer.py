def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(dict.fromkeys(string_of_chars))
    distinct_chars.sort(key=ord)
    n_greatest_chars = distinct_chars[-3:]
    return n_greatest_chars