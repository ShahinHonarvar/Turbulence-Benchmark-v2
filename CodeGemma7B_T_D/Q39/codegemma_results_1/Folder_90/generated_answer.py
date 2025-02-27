def return_n_greatest_chars(string):
    res = sorted([*string], reverse=True)
    return res[:24]