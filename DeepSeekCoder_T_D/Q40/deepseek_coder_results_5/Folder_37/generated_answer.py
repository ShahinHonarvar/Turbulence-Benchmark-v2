def return_n_smallest_chars(s):
    return sorted(sorted(s)[:26], reverse=True)