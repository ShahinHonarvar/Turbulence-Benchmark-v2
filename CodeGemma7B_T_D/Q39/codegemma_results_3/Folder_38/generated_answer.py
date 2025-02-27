def return_n_greatest_chars(str_dist_chars):
    return sorted(str_dist_chars, key=ord, reverse=True)[:45]