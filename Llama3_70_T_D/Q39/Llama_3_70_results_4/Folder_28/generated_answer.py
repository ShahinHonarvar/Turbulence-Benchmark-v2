def return_n_greatest_chars(s):
    return sorted(sorted(s)[-3:], reverse=False)