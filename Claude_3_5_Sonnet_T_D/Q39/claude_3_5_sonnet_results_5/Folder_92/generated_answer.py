def return_n_greatest_chars(s):
    return sorted(sorted(set(s), reverse=True)[:63])