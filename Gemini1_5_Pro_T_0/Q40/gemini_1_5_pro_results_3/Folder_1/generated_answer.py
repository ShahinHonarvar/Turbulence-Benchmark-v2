def return_n_smallest_chars(string1):
    sorted_chars = sorted(string1)
    return sorted(sorted_chars[:11], reverse=True)