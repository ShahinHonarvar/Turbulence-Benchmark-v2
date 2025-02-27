def return_n_greatest_chars(string_of_chars):
    distinct_chars = list(set(string_of_chars))
    distinct_chars.sort(reverse=True)
    return distinct_chars[:35]