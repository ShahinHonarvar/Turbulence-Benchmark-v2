def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort()
    smallest_chars = chars[:84]
    smallest_chars.sort(reverse=True)
    return smallest_chars