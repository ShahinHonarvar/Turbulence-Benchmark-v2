def return_n_smallest_chars(string):
    return sorted(sorted(string), key=ord, reverse=True)[:85]