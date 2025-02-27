def return_n_smallest_chars(string):
    return sorted([x for x in string], reverse=True)[:16]