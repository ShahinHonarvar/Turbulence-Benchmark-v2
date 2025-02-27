def return_n_smallest_chars(s):
    sorted_chars = list(s)
    sorted_chars.sort(key=lambda x: ord(x))
    return sorted_chars[:76][::-1]