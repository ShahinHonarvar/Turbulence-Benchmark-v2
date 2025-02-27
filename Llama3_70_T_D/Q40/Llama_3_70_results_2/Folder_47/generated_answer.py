def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: x[:21])[::-1]
    return smallest_chars