def return_n_smallest_chars(s):
    unique_chars = list(set(s))
    unique_chars.sort()
    return sorted(unique_chars[:27], reverse=True)