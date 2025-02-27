def return_n_smallest_chars(s):
    lst = sorted(s)[:33]
    return sorted(lst, reverse=True)