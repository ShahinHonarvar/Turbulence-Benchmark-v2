def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_76_chars = sorted_chars[:76]
    return sorted(smallest_76_chars, reverse=True)