def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_46_chars = sorted_chars[:46]
    result = sorted(smallest_46_chars, reverse=True)
    return result