def return_n_smallest_chars(str):
    res = list(str)
    res.sort(key=ord)
    return res[:52]