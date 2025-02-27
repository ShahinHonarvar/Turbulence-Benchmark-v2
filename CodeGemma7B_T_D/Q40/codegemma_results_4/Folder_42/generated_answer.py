def return_n_smallest_chars(chars):
    lst = sorted(chars, key=ord, reverse=True)
    return lst[len(lst) - 59:]