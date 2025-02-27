def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:56]
    smallest_chars.sort(reverse=True)
    return smallest_chars