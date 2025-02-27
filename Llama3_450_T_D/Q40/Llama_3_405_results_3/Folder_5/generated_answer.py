def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: ord(x))[:46]
    smallest_chars.sort(reverse=True)
    return smallest_chars