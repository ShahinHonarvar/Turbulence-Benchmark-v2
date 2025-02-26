def return_n_smallest_chars(input_string):
    unique_chars = set(input_string)
    sorted_chars = sorted(unique_chars, key=ord)[:79]
    return sorted(sorted_chars, reverse=True)