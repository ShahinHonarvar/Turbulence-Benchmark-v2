def return_n_smallest_chars(string):
    list_of_chars = list(string)
    list_of_chars.sort(key=ord)
    return list_of_chars[:36][::-1]