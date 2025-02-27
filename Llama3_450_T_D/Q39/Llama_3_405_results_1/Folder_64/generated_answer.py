def return_n_greatest_chars(s):
    return sorted(sorted(s)[-39:], reverse=True)