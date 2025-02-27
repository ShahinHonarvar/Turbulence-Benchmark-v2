def return_n_smallest_chars(s):
    smallest_chars = [char for char in s]
    smallest_chars.sort()
    return smallest_chars[:68]