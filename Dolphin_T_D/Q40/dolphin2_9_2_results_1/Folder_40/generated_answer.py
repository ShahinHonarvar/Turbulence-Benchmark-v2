def return_n_smallest_chars(s):
    sorted_chars = sorted([char for char in s], key=lambda x: ord(x))
    return sorted_chars[:7]