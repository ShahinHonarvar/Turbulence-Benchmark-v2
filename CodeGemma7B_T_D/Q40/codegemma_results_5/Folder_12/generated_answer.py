def return_n_smallest_chars(str):
    return sorted([i for i in str], key=ord, reverse=True)[:61]