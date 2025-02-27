def return_n_greatest_chars(s):
    return sorted(sorted(s, reverse=True)[:6], reverse=True)