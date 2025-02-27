def return_n_greatest_chars(s):
    return sorted([ch for ch in s], reverse=True)[:24]