def return_n_smallest_chars(string):
    unique_chars = sorted(set(string), key=ord)
    return sorted(unique_chars[:26], reverse=True)