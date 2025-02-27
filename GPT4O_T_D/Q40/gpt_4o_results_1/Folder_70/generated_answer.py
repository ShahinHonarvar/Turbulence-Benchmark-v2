def return_n_smallest_chars(s):
    two_smallest = sorted(s)[:2]
    return sorted(two_smallest, reverse=True)