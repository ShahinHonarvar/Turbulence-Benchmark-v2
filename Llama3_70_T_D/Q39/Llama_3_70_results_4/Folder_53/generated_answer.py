def return_n_greatest_chars(s):
    return sorted(sorted(s)[-19:], reverse=False)