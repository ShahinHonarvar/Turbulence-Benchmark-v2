def return_n_smallest_chars(string):
    list_of_chars = [char for char in string]
    list_of_chars.sort()
    return list_of_chars[:20]