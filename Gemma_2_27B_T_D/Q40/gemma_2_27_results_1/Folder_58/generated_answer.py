def return_n_smallest_chars(string):
    return sorted([c for c in string], reverse=True)[:49]