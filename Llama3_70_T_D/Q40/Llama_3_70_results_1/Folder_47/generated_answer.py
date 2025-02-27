def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: x[:1])[0:21]
    smallest_chars.sort(reverse=True)
    return smallest_chars