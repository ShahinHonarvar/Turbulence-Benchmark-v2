def return_n_smallest_chars(str):
    lst = list(str)
    lst.sort(key=ord)
    return lst[:46]