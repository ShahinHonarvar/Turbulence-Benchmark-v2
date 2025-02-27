def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    return sorted(sorted_s[:56], reverse=True)