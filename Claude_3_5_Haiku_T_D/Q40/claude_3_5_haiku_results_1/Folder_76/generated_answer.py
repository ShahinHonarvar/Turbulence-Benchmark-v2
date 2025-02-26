def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string), key=ord)[:3]
    return sorted(sorted_chars, reverse=True)