def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:56]
    return sorted_chars