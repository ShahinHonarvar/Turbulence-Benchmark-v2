def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted(sorted_chars[:21], reverse=True)