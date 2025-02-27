def return_n_greatest_chars(string_of_chars):
    unique_chars = list(set(string_of_chars))
    sorted_chars = sorted(unique_chars, reverse=True)
    truncated_chars = sorted_chars[:20]
    return truncated_chars