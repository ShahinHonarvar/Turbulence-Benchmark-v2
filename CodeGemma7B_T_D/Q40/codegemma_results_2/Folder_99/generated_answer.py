def return_n_smallest_chars(string):
    return sorted(string, key=ord, reverse=True)[:35]