def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    n = min(len(sorted_chars), 52)
    return sorted(sorted_chars[:n], reverse=True)