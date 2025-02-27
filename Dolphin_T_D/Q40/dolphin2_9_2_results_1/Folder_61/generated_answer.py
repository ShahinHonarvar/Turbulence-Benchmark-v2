def return_n_smallest_chars(s):
    list_chars = list(s)
    sorted_chars = sorted(list_chars, key=lambda x: ord(x))
    return sorted_chars[::-1][:66]