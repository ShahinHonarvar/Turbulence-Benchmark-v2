def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=ord, reverse=True)[:9]
    return sorted_s