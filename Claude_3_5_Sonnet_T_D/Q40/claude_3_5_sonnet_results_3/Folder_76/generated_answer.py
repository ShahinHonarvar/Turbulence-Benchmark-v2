def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_three = sorted_chars[:3]
    return sorted(smallest_three, reverse=True)