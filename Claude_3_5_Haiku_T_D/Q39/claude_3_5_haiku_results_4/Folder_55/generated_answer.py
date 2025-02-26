def return_n_greatest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, reverse=True)
    return sorted_chars[:75]