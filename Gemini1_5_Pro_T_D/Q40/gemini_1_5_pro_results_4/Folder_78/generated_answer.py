def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    return sorted(sorted_chars[:43], reverse=True)