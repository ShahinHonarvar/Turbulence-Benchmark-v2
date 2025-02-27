def return_n_greatest_chars(s):
    return sorted(sorted(list(s), reverse=True)[:2])[::-1]