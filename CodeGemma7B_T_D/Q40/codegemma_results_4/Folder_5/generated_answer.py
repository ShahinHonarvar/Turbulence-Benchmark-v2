def return_n_smallest_chars(a):
    list_a = list(a)
    list_a.sort(key=ord, reverse=True)
    return list_a[:46]