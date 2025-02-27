def return_n_smallest_chars(string):
    list_of_chars = list(string)
    list_of_chars.sort(reverse=True)
    return list_of_chars[:46]