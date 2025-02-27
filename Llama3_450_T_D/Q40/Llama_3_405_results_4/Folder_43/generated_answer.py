def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_56_chars = sorted_chars[:56]
    smallest_56_chars.sort(reverse=True)
    return smallest_56_chars