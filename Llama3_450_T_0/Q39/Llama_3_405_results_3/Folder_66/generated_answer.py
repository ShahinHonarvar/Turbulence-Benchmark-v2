def return_n_greatest_chars(s):
    return sorted(sorted(s)[-33:], reverse=True)