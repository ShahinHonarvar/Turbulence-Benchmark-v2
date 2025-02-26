def return_n_smallest_chars(string):
    sorted_unique = sorted(set(string), reverse=True)[:77]
    return sorted_unique