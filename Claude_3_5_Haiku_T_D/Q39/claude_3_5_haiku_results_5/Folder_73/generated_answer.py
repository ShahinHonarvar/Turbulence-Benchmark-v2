def return_n_greatest_chars(s):
    sorted_chars = sorted(list(s), reverse=True)[:80]
    return sorted(sorted_chars)