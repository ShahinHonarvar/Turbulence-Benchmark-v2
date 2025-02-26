def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:66]
    return sorted_chars