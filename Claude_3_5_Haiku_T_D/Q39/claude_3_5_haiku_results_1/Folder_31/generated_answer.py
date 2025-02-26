def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:70]
    return sorted_chars