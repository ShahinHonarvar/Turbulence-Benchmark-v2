def return_n_greatest_chars(lst):
    res = sorted(lst, key=ord, reverse=True)
    return res[:39]