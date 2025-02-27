def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted_chars[-60:]