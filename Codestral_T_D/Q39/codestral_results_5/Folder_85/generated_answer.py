def return_n_greatest_chars(s):
    sorted_chars = sorted(list(s), reverse=True)
    return sorted_chars[:85]