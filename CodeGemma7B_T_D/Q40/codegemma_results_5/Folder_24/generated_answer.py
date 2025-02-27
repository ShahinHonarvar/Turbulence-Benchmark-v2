def return_n_smallest_chars(s):
    sorted_list = sorted(s, key=ord, reverse=True)
    return sorted_list[:32]