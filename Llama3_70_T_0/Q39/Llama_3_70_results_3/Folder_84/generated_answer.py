def return_n_greatest_chars(s):
    return sorted(sorted(s)[-10:], reverse=False)