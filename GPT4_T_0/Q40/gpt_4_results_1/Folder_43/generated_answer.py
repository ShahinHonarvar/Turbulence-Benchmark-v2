def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_chars = sorted_chars[:56]
    smallest_chars.sort(reverse=True)
    return smallest_chars