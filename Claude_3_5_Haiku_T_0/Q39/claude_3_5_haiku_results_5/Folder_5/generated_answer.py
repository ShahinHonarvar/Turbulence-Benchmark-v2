def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)
    return sorted_chars[:46]