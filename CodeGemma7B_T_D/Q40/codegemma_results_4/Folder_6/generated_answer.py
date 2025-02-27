def return_n_smallest_chars(str):
    return sorted(str, key=ord, reverse=True)[:47]