def return_n_smallest_chars(str):
    list_of_chars = sorted(str, key=ord, reverse=True)
    return list_of_chars[:46]