def return_n_smallest_chars(string):
    return sorted(list(string), key=ord, reverse=True)[:82]