def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:84]
    smallest_chars.sort(reverse=True)
    return smallest_chars