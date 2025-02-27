def return_n_greatest_chars(s):
    return sorted(s, reverse=True)[:3][::-1]