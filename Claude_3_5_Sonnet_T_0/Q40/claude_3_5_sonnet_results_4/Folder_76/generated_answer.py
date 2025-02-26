def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_three = sorted_chars[:3]
    return sorted(smallest_three, reverse=True)