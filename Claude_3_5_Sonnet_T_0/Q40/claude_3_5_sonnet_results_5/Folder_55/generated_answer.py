def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_75 = sorted_chars[:75]
    return sorted(smallest_75, reverse=True)