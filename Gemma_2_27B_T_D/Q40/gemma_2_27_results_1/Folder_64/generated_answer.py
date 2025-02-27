def return_n_smallest_chars(input_string):
    return sorted([c for c in input_string], reverse=True)[:39]