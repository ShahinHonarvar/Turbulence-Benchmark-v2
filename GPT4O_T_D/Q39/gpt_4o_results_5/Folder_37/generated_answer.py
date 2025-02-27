def return_n_greatest_chars(s):
    res = sorted(s, reverse=True)
    return res[:26]