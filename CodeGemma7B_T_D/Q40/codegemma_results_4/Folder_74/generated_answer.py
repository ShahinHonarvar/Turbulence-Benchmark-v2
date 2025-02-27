def return_n_smallest_chars(txt):
    lst = sorted([i for i in txt], key=ord)[:5]
    return lst