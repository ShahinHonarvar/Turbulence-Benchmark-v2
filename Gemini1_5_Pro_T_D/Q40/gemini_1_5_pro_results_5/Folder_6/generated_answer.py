def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))
    return sorted(sorted_chars[:47], reverse=True)