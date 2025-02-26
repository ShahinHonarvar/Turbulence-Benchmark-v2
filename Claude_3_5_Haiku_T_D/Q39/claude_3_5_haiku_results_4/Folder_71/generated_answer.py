def return_n_greatest_chars(s):
    sorted_unique_chars = sorted(set(s))
    return sorted_unique_chars[-14:]