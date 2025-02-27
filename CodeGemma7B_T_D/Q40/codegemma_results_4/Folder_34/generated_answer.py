def return_n_smallest_chars(string):
    list_of_sorted_chars = sorted(string, key=ord)
    return list_of_sorted_chars[:9]