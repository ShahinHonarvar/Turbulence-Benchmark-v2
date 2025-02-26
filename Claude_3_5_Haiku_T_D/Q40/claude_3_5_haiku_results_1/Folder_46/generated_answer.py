def return_n_smallest_chars(string):
    sorted_chars = sorted(list(string))
    return sorted(sorted_chars[:54], reverse=True)