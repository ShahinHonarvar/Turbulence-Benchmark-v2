def return_n_greatest_chars(s):
    return sorted(sorted(s)[::-1][:10])